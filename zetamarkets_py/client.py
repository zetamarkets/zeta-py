import asyncio
import json
import logging
import time
from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable, Optional, cast
import based58

import websockets
from anchorpy import Event, EventParser, Provider, Wallet
from anchorpy.provider import DEFAULT_OPTIONS
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment, Confirmed
from solana.rpc.core import RPCException
from solana.rpc.types import TxOpts
from solana.rpc.websocket_api import SolanaWsClientProtocol, connect, Data
from solders.instruction import Instruction
from solders.message import MessageV0
from solders.pubkey import Pubkey
from solders.rpc.config import RpcTransactionLogsFilterMentions
from solders.transaction import VersionedTransaction

from zetamarkets_py import constants, pda, utils
from zetamarkets_py.events import (
    LiquidationEvent,
    OrderCompleteEvent,
    PlaceOrderEvent,
    PlaceOrderEventWithArgs,
    TradeEvent,
    TradeEventWithPlacePerpOrderArgs,
)
from zetamarkets_py.exchange import Exchange
from zetamarkets_py.orderbook import Orderbook
from zetamarkets_py.serum_client.accounts.orderbook import OrderbookAccount
from zetamarkets_py.types import Asset, Network, OrderArgs, OrderOptions, Position, Side
from zetamarkets_py.zeta_client.accounts.cross_margin_account import CrossMarginAccount
from zetamarkets_py.zeta_client.errors import from_tx_error
from zetamarkets_py.zeta_client.instructions import (
    cancel_all_market_orders,
    cancel_order,
    deposit_v2,
    initialize_cross_margin_account,
    initialize_cross_margin_account_manager,
    initialize_open_orders_v3,
    place_perp_order_v3,
)

from jsonrpcclient import request

# TODO: add transactionSubscribe (do we even need this right now?)
# TODO: add Binance heartbeat to websocket
# TODO: add better ws error handling and reconnection
# TODO: add docstrings for most methods
# TODO: add docs to examples in readthedocs
# TODO: add client_order_id to PlaceOrderEvent
# TODO: implement withdraw and liquidation
# TODO: add logging to exchange
# TODO: implement priority fees to exchange


@dataclass
class Client:
    """
    Cross margin client
    """

    provider: Provider
    network: Network
    connection: AsyncClient
    endpoint: str
    ws_endpoint: str
    exchange: Exchange

    margin_account: Optional[CrossMarginAccount]

    _margin_account_address: Optional[Pubkey]
    _open_orders_addresses: Optional[dict[Asset, Pubkey]]
    _margin_account_manager_address: Optional[Pubkey]
    _user_usdc_address: Optional[Pubkey]
    _combined_vault_address: Pubkey
    _combined_socialized_loss_address: Pubkey
    _logger: logging.Logger
    _account_exists_cache: dict[Pubkey, bool] = field(default_factory=dict)

    @classmethod
    async def load(
        cls,
        endpoint: str = None,
        ws_endpoint: Optional[str] = None,
        commitment: Commitment = Confirmed,
        wallet: Optional[Wallet] = None,
        assets: list[Asset] = Asset.all(),
        tx_opts: TxOpts = DEFAULT_OPTIONS,
        network: Network = Network.MAINNET,
    ):
        """
        Create a new client
        """
        logger = logging.getLogger(f"{__name__}.{cls.__name__}")
        if endpoint is None:
            endpoint = utils.cluster_endpoint(network)
        if ws_endpoint is None:
            ws_endpoint = utils.http_to_ws(endpoint)
        connection = AsyncClient(endpoint=endpoint, commitment=commitment, blockhash_cache=False)
        exchange = await Exchange.load(
            network=network,
            connection=connection,
            assets=assets,
        )
        if wallet is None:
            wallet = Wallet.dummy()
            logger.warning("Client in read-only mode, pass in `wallet` to enable transactions")
            _margin_account_manager_address = None
            _user_usdc_address = None
            _margin_account_address = None
            margin_account = None
            _open_orders_addresses = None
        else:
            _margin_account_manager_address = pda.get_cross_margin_account_manager_address(
                exchange.program_id, wallet.public_key
            )
            _user_usdc_address = pda.get_associated_token_address(wallet.public_key, constants.USDC_MINT[network])
            _margin_account_address = pda.get_margin_account_address(exchange.program_id, wallet.public_key, 0)
            margin_account = await CrossMarginAccount.fetch(
                connection, _margin_account_address, connection.commitment, exchange.program_id
            )
            _open_orders_addresses = {}
            for asset in assets:
                open_orders_address = pda.get_open_orders_address(
                    exchange.program_id,
                    constants.MATCHING_ENGINE_PID[network],
                    exchange.markets[asset].address,
                    _margin_account_address,
                )
                _open_orders_addresses[asset] = open_orders_address
        provider = Provider(
            connection,
            wallet,
            tx_opts,
        )

        # additional addresses to cache
        _combined_vault_address = pda.get_combined_vault_address(exchange.program_id)
        _combined_socialized_loss_address = pda.get_combined_socialized_loss_address(exchange.program_id)

        return cls(
            provider,
            network,
            connection,
            endpoint,
            ws_endpoint,
            exchange,
            margin_account,
            _margin_account_address,
            _open_orders_addresses,
            _margin_account_manager_address,
            _user_usdc_address,
            _combined_vault_address,
            _combined_socialized_loss_address,
            logger,
        )

    async def _check_user_usdc_account_exists(self):
        if self._margin_account_manager_address in self._account_exists_cache:
            return self._account_exists_cache[self._margin_account_manager_address]
        resp = await self.connection.get_account_info(self._user_usdc_address)
        exists = resp.value is not None
        self._account_exists_cache[self._margin_account_manager_address] = exists
        return exists

    async def _check_margin_account_manager_exists(self):
        if self._margin_account_manager_address in self._account_exists_cache:
            return self._account_exists_cache[self._margin_account_manager_address]
        resp = await self.connection.get_account_info(self._user_usdc_address)
        exists = resp.value is not None
        self._account_exists_cache[self._margin_account_manager_address] = exists
        return exists

    async def _check_margin_account_exists(self):
        if self._margin_account_manager_address in self._account_exists_cache:
            return self._account_exists_cache[self._margin_account_manager_address]
        account = await CrossMarginAccount.fetch(self.connection, self._margin_account_address)
        exists = account is not None
        self._account_exists_cache[self._margin_account_manager_address] = exists
        self.margin_account = account
        return exists

    async def _check_open_orders_account_exists(self, asset: Asset):
        open_orders_address = self._open_orders_addresses[asset]
        if open_orders_address in self._account_exists_cache:
            return self._account_exists_cache[open_orders_address]
        resp = await self.connection.get_account_info(open_orders_address)
        exists = resp.value is not None
        self._account_exists_cache[open_orders_address] = exists
        return exists

    async def fetch_balance(self):
        margin_account = await self.margin_account.fetch(
            self.connection,
            self._margin_account_address,
            self.connection.commitment,
            self.exchange.program_id,
        )
        balance = utils.convert_fixed_int_to_decimal(margin_account.balance)
        return balance

    async def fetch_position(self, asset: Asset):
        if self.margin_account is None or self._margin_account_address is None:
            raise Exception("Margin account not loaded, cannot fetch position")
        margin_account = await self.margin_account.fetch(
            self.connection, self._margin_account_address, self.connection.commitment, self.exchange.program_id
        )
        if margin_account is None:
            raise Exception("Margin account not found, cannot fetch position")
        position = Position(
            utils.convert_fixed_lot_to_decimal(margin_account.product_ledgers[asset.to_index()].position.size),
            utils.convert_fixed_int_to_decimal(
                margin_account.product_ledgers[asset.to_index()].position.cost_of_trades
            ),
        )
        return position

    async def fetch_open_orders(self, asset: Asset):
        if self._open_orders_addresses is None:
            raise Exception("Open orders accounts not loaded, cannot fetch open orders")
        oo = await self.exchange.markets[asset].load_orders_for_owner(self._open_orders_addresses[asset])
        return oo

    async def _account_subscribe(
        self,
        address: Pubkey,
        ws_endpoint: str,
        commitment: Commitment,
        callback: Callable[[bytes], Any],
        max_retries: int = 3,
        encoding: str = "base64+zstd",
    ) -> None:
        retries = max_retries
        while True:
            try:
                async with connect(ws_endpoint) as ws:
                    solana_ws: SolanaWsClientProtocol = cast(SolanaWsClientProtocol, ws)
                    await solana_ws.account_subscribe(
                        address,
                        commitment=commitment,
                        encoding=encoding,
                    )
                    first_resp = await solana_ws.recv()
                    subscription_id = cast(int, first_resp[0].result)
                    async for msg in ws:
                        try:
                            account_bytes = cast(bytes, msg[0].result.value.data)  # type: ignore
                            await callback(account_bytes)
                        except Exception as e:
                            self._logger.error(f"Error processing account data: {e}")
                            break
                    await solana_ws.account_unsubscribe(subscription_id)
            except asyncio.CancelledError:
                self._logger.info("WebSocket subscription task cancelled.")
                break
            except websockets.exceptions.ConnectionClosed:
                self._logger.error("WebSocket connection closed unexpectedly. Attempting to reconnect...")
                continue
            except Exception as e:
                self._logger.error(f"Error subscribing to {self.__class__.__name__}: {e}")
                retries -= 1
                if retries <= 0:
                    self._logger.error("Max retries reached. Unable to subscribe to account.")
                    break
                await asyncio.sleep(2)  # Pause for a while before retrying

    async def subscribe_orderbook(
        self, asset: Asset, side: Side, callback: Callable[[Orderbook], Awaitable[Any]], max_retries: int = 3
    ):
        ws_endpoint = utils.cluster_endpoint(self.network, ws=True)
        address = (
            self.exchange.markets[asset]._market_state.bids
            if side == Side.Bid
            else self.exchange.markets[asset]._market_state.asks
        )

        # Wrap callback in order to parse account data correctly
        async def _callback(data: bytes):
            account = OrderbookAccount.decode(data)
            orderbook = Orderbook(side, account, self.exchange.markets[asset]._market_state)
            return await callback(orderbook)

        self._logger.info(f"Subscribing to Orderbook:{side}.")
        await self._account_subscribe(address, ws_endpoint, self.connection.commitment, _callback, max_retries)

    async def subscribe_transactions(
        self,
        place_order_with_args_callback: Callable[[PlaceOrderEventWithArgs], Awaitable[Any]] = None,
        trade_event_with_place_perp_order_args_callback: Callable[[TradeEventWithPlacePerpOrderArgs], Awaitable[Any]] = None,
        trade_event_callback: Callable[[TradeEvent], Awaitable[Any]] = None,
        order_complete_event_callback: Callable[[OrderCompleteEvent], Awaitable[Any]] = None,
        max_retries: int = 3,
    ):
        retries = max_retries
        while retries > 0:
            try:
                async with websockets.connect(self.ws_endpoint + "/whirligig") as ws:
                    transaction_subscribe = request(
                        "transactionSubscribe",
                        params=[
                            {
                                "mentions": [str(self._margin_account_address)],
                                "failed": False,
                                "vote": False,
                            },
                            {
                                "commitment": str(self.connection.commitment),
                            },
                        ],
                    )
                     
                    await ws.send(json.dumps(transaction_subscribe))
                    first_resp = await ws.recv()
                    subscription_id = cast(int, first_resp)

                    async for msg in ws:
                        try:
                            await self.parse_transaction_payload(msg, place_order_with_args_callback, trade_event_with_place_perp_order_args_callback, trade_event_callback, order_complete_event_callback)

                        except Exception as e:
                            self._logger.error(f"Error processing transaction data: {e}")
                            break

                    request(
                        "transactionUnsubscribe",
                        params=[subscription_id],
                    )
                    await ws.send(json.dumps(transaction_subscribe))

            except asyncio.CancelledError:
                self._logger.info("WebSocket subscription task cancelled.")
                break
            except websockets.exceptions.ConnectionClosed:
                self._logger.error("WebSocket connection closed unexpectedly. Attempting to reconnect...")
                continue
            except Exception as e:
                self._logger.error(f"Error subscribing to {self.__class__.__name__}: {e}")
                retries -= 1
                if retries <= 0:
                    self._logger.error("Max retries reached. Unable to subscribe to transactions.")
                    break
                await asyncio.sleep(2)  # Pause for a while before retrying

    # TODO: maybe at some point support subscribing to all exchange events, not just margin account
    async def subscribe_events(
        self,
        place_order_callback: Callable[[PlaceOrderEvent], Awaitable[Any]] = None,
        order_complete_callback: Callable[[OrderCompleteEvent], Awaitable[Any]] = None,
        trade_callback: Callable[[TradeEvent], Awaitable[Any]] = None,
        liquidation_callback: Callable[[LiquidationEvent], Awaitable[Any]] = None,
        max_retries: int = 3,
    ):
        retries = max_retries
        while retries > 0:
            try:
                async with connect(self.ws_endpoint) as ws:
                    solana_ws: SolanaWsClientProtocol = cast(SolanaWsClientProtocol, ws)
                    # Subscribe to logs that mention the margin account
                    await solana_ws.logs_subscribe(
                        commitment=self.connection.commitment,
                        filter_=RpcTransactionLogsFilterMentions(self._margin_account_address),
                    )
                    first_resp = await solana_ws.recv()
                    subscription_id = cast(int, first_resp[0].result)
                    async for msg in ws:
                        try:
                            await self.parse_event_payload(msg, place_order_callback, order_complete_callback, trade_callback, liquidation_callback)
                            
                        except Exception as e:
                            self._logger.error(f"Error processing event data: {e}")
                            break
                    await solana_ws.logs_unsubscribe(subscription_id)
            except asyncio.CancelledError:
                self._logger.info("WebSocket subscription task cancelled.")
                break
            except websockets.exceptions.ConnectionClosed:
                self._logger.error("WebSocket connection closed unexpectedly. Attempting to reconnect...")
                continue
            except Exception as e:
                self._logger.error(f"Error subscribing to {self.__class__.__name__}: {e}")
                retries -= 1
                if retries <= 0:
                    self._logger.error("Max retries reached. Unable to subscribe to events.")
                    break
                await asyncio.sleep(2)  # Pause for a while before retrying

    async def parse_event_payload(self, msg: Data, place_order_callback: Callable[[PlaceOrderEvent], Awaitable[Any]] = None,
        order_complete_callback: Callable[[OrderCompleteEvent], Awaitable[Any]] = None,
        trade_callback: Callable[[TradeEvent], Awaitable[Any]] = None,
        liquidation_callback: Callable[[LiquidationEvent], Awaitable[Any]] = None):

        logs = cast(list[str], msg[0].result.value.logs)  # type: ignore
        parser = EventParser(self.exchange.program_id, self.exchange.program.coder)
        parsed: list[Event] = []
        parser.parse_logs(logs, lambda evt: parsed.append(evt))
        for event in parsed:
            if event.name.startswith(PlaceOrderEvent.__name__):
                place_order_event = PlaceOrderEvent.from_event(event)
                if place_order_event.margin_account == self._margin_account_address:
                    if place_order_callback is not None:
                        await place_order_callback(place_order_event)
            elif event.name.startswith(OrderCompleteEvent.__name__):
                order_complete_event = OrderCompleteEvent.from_event(event)
                if order_complete_event.margin_account == self._margin_account_address:
                    if order_complete_callback is not None:
                        await order_complete_callback(order_complete_event)
            elif event.name.startswith(TradeEvent.__name__):
                trade_event = TradeEvent.from_event(event)
                if trade_event.margin_account == self._margin_account_address:
                    if trade_callback is not None:
                        await trade_callback(trade_event)
            elif event.name.startswith(LiquidationEvent.__name__):
                liquidation_event = LiquidationEvent.from_event(event)
                if liquidation_event.liquidatee_margin_account == self._margin_account_address:
                    if liquidation_callback is not None:
                        await liquidation_callback(liquidation_event)
            else:
                pass

    async def parse_transaction_payload(self, msg: Data, place_order_with_args_callback: Callable[[PlaceOrderEventWithArgs], Awaitable[Any]] = None,
        trade_event_with_place_perp_order_args_callback: Callable[[TradeEventWithPlacePerpOrderArgs], Awaitable[Any]] = None,
        trade_event_callback: Callable[[TradeEvent], Awaitable[Any]] = None,
        order_complete_event_callback: Callable[[OrderCompleteEvent], Awaitable[Any]] = None):

        parser = EventParser(self.exchange.program_id, self.exchange.program.coder)
                                    
        jsonMsg = json.loads(msg)
        txValue = jsonMsg['params']['result']['value'] 

        logMessages = txValue['meta']['logMessages']

        message = txValue['transaction']['message']
        if isinstance(message[0], int) or 'instructions' not in message[0]:
            messageIndexed = message[1]
        else:
            messageIndexed = message[0]
        
        ixs = messageIndexed['instructions'][1:]
        ixArgs = []
        ixNames = []

        for ix in ixs:
            accKeysRaw = messageIndexed['accountKeys'][1:]                                
            accountKeys = [str(based58.b58encode(bytes(a)), encoding='utf-8') for a in accKeysRaw]

            loadedAddresses = txValue['meta']['loadedAddresses']
            loadedAddressesList = accountKeys + loadedAddresses['writable'] + loadedAddresses['readonly']
            ownerAddress = loadedAddressesList[ix['programIdIndex']]
            if ownerAddress != str(constants.ZETA_PID[self.network]):
                ixArgs.append(None)
                ixNames.append(None)
                continue
            data = self.exchange.program.coder.instruction.parse(bytes(ix['data'][1:]))
            ixArgs.append(data.data)
            ixNames.append(data.name)

        # Split logMessages every time we see "invoke [1]"
        splitLogMessages = []
        splitIndices = []
        for i in range(len(logMessages)):
            if logMessages[i] == 'Log truncated':
                raise Exception("Logs truncated, missing event data")
            if logMessages[i].endswith('invoke [1]'):
                splitIndices.append(i)
        
        splitLogMessages = [logMessages[i:j] for i, j in zip([0]+splitIndices, splitIndices+[None])]
        if len(splitLogMessages) > 0:
            splitLogMessages = splitLogMessages[1:]

        if len(ixArgs) != len(splitLogMessages) or len(ixNames) != len(splitLogMessages):
            raise Exception("Mismatched transation info lengths")

        # For each individual instruction, find the ix name and the events
        for i in range(len(splitLogMessages)):

            # # First log line will always be "...invoke [1]", second will be "Program log: Instruction: <ix_name>"
            ixName = ixNames[i]
            ixArg = ixArgs[i]

            if ixName is None or ixArg is None:
                continue

            chunk = splitLogMessages[i]
            events: list[Event] = []
            parser.parse_logs(chunk, lambda evt: events.append(evt))

            # Depending on the instruction and event we can get different data from the args
            for event in events:

                # Skip event that aren't for our account but mention our account
                # eg if we do a taker trade, we want to skip the maker crank events
                if str(event.data.margin_account) != str(self._margin_account_address):
                    continue

                if ixName.startswith('place_perp_order'):
                    if event.name.startswith(TradeEvent.__name__):
                        if trade_event_with_place_perp_order_args_callback is not None:
                            await trade_event_with_place_perp_order_args_callback(TradeEventWithPlacePerpOrderArgs.from_event_and_args(event, ixArg))
                    elif event.name.startswith(PlaceOrderEvent.__name__):
                        if place_order_with_args_callback is not None:
                            await place_order_with_args_callback(PlaceOrderEventWithArgs.from_event_and_args(event, ixArg))
                    elif event.name.startswith(OrderCompleteEvent.__name__):
                        if order_complete_event_callback is not None:
                            await order_complete_event_callback(OrderCompleteEvent.from_event(event))
                    
                elif ixName.startswith('crank_event_queue'):
                    if event.name.startswith(TradeEvent.__name__):
                        if trade_event_callback is not None:
                            await trade_event_callback(TradeEvent.from_event(event))
                    elif event.name.startswith(OrderCompleteEvent.__name__):
                        if order_complete_event_callback is not None:
                            await order_complete_event_callback(OrderCompleteEvent.from_event(event))

                elif ixName.startswith('cancel_'):
                    if event.name.startswith(OrderCompleteEvent.__name__):
                        if order_complete_event_callback is not None:
                            await order_complete_event_callback(OrderCompleteEvent.from_event(event))

    # Instructions

    async def deposit(self, amount: float, subaccount_index: int = 0):
        ixs = []
        if not await self._check_margin_account_manager_exists():
            self._logger.info("User has no cross-margin account manager, creating one...")
            ixs.append(self._init_margin_account_manager_ix())
        # Create margin account if user doesn't have one
        if not await self._check_margin_account_exists():
            self._logger.info("User has no cross-margin account, creating one...")
            ixs.append(self._init_margin_account_ix(subaccount_index))
        # Check they have an existing USDC account
        if await self._check_user_usdc_account_exists():
            ixs.append(self._deposit_ix(amount))
        else:
            raise Exception("User has no USDC, cannot deposit to margin account")

        self._logger.info(f"Depositing {amount} USDC to margin account")
        return await self._send_versioned_transaction(ixs)

    def _init_margin_account_manager_ix(self) -> Instruction:
        if self._margin_account_manager_address is None:
            raise Exception("Margin account manager address not loaded, cannot deposit")
        return initialize_cross_margin_account_manager(
            {
                "cross_margin_account_manager": self._margin_account_manager_address,
                "authority": self.provider.wallet.public_key,
                "payer": self.provider.wallet.public_key,
                "zeta_program": self.exchange.program_id,
            },
            self.exchange.program_id,
        )

    def _init_margin_account_ix(self, subaccount_index: int = 0) -> Instruction:
        if self._margin_account_address is None or self._margin_account_manager_address is None:
            raise Exception("Margin account address not loaded, cannot deposit")
        return initialize_cross_margin_account(
            {"subaccount_index": subaccount_index},
            {
                "cross_margin_account": self._margin_account_address,
                "cross_margin_account_manager": self._margin_account_manager_address,
                "authority": self.provider.wallet.public_key,
                "payer": self.provider.wallet.public_key,
                "zeta_program": self.exchange.program_id,
            },
            self.exchange.program_id,
        )

    def _deposit_ix(self, amount: float) -> Instruction:
        if self._user_usdc_address is None or self._margin_account_address is None:
            raise Exception("User USDC address not loaded, cannot deposit")
        return deposit_v2(
            {"amount": utils.convert_decimal_to_fixed_int(amount)},
            {
                "margin_account": self._margin_account_address,
                "vault": self._combined_vault_address,
                "user_token_account": self._user_usdc_address,
                "socialized_loss_account": self._combined_socialized_loss_address,
                "authority": self.provider.wallet.public_key,
                "state": self.exchange._state_address,
                "pricing": self.exchange._pricing_address,
            },
            self.exchange.program_id,
        )

    # TODO: withdraw (and optionally close)
    async def withdraw(self):
        raise NotImplementedError

    def _init_open_orders_ix(self, asset: Asset) -> Instruction:
        if asset not in self.exchange.assets:
            raise Exception(f"Asset {asset.name} not loaded into client, cannot initialize open orders")
        if self._open_orders_addresses is None or self._margin_account_address is None:
            raise Exception("Open orders address not loaded, cannot place order")
        return initialize_open_orders_v3(
            {"asset": asset.to_program_type()},
            {
                "state": self.exchange._state_address,
                "dex_program": constants.MATCHING_ENGINE_PID[self.network],
                "open_orders": self._open_orders_addresses[asset],
                "cross_margin_account": self._margin_account_address,
                "authority": self.provider.wallet.public_key,
                "payer": self.provider.wallet.public_key,
                "market": self.exchange.markets[asset].address,
                "serum_authority": self.exchange._serum_authority_address,
                "open_orders_map": pda.get_open_orders_map_address(
                    self.exchange.program_id, self._open_orders_addresses[asset]
                ),
            },
            self.exchange.program_id,
        )

    def _place_order_ix(
        self,
        asset: Asset,
        price: float,
        size: float,
        side: Side,
        order_opts: OrderOptions = None,
    ) -> Instruction:
        if order_opts is None:
            order_opts = OrderOptions()

        unix_timestamp = int(time.time())
        tif_offset = (
            utils.get_tif_offset(
                order_opts.expiry_ts,
                self.exchange.markets[asset]._market_state.epoch_length,
                unix_timestamp,  # self.exchange.clock.account.unix_timestamp,
            )
            if order_opts.expiry_ts
            else None
        )

        if asset not in self.exchange.assets:
            raise Exception(f"Asset {asset.name} not loaded into client, cannot place order")
        if self._margin_account_address is None:
            raise Exception("Margin account address not loaded, cannot place order")
        if self._open_orders_addresses is None:
            raise Exception("Open orders addresses not loaded, cannot place order")

        return place_perp_order_v3(
            {
                "price": utils.convert_decimal_to_fixed_int(price),
                "size": utils.convert_decimal_to_fixed_lot(size),
                "side": side.to_program_type(),
                "order_type": order_opts.order_type.to_program_type(),
                "client_order_id": order_opts.client_order_id,
                "tif_offset": tif_offset,
                "tag": order_opts.tag,
                "asset": asset.to_program_type(),
            },
            {
                "state": self.exchange._state_address,
                "pricing": self.exchange._pricing_address,
                "margin_account": self._margin_account_address,
                "authority": self.provider.wallet.public_key,
                "dex_program": constants.MATCHING_ENGINE_PID[self.network],
                "serum_authority": self.exchange._serum_authority_address,
                "open_orders": self._open_orders_addresses[asset],
                "market_accounts": {
                    "market": self.exchange.markets[asset].address,
                    "request_queue": self.exchange.markets[asset]._market_state.request_queue,
                    "event_queue": self.exchange.markets[asset]._market_state.event_queue,
                    "bids": self.exchange.markets[asset]._market_state.bids,
                    "asks": self.exchange.markets[asset]._market_state.asks,
                    "coin_vault": self.exchange.markets[asset]._market_state.base_vault,
                    "pc_vault": self.exchange.markets[asset]._market_state.quote_vault,
                    "order_payer_token_account": self.exchange.markets[asset]._quote_zeta_vault_address
                    if side == Side.Bid
                    else self.exchange.markets[asset]._base_zeta_vault_address,
                    "coin_wallet": self.exchange.markets[asset]._base_zeta_vault_address,
                    "pc_wallet": self.exchange.markets[asset]._quote_zeta_vault_address,
                },
                "oracle": self.exchange.pricing.oracles[asset.to_index()],
                "oracle_backup_feed": self.exchange.pricing.oracle_backup_feeds[asset.to_index()],
                "oracle_backup_program": constants.CHAINLINK_PID,
                "market_mint": self.exchange.markets[asset]._market_state.quote_mint
                if side == Side.Bid
                else self.exchange.markets[asset]._market_state.base_mint,
                "mint_authority": self.exchange._mint_authority_address,
                "perp_sync_queue": self.exchange.pricing.perp_sync_queues[asset.to_index()],
            },
            self.exchange.program_id,
        )

    async def cancel_order(self, asset: Asset, order_id: int, side: Side):
        ixs = [self._cancel_order_ix(asset, order_id, side)]
        self._logger.info(f"Cancelling order {order_id} for {asset}")
        return await self._send_versioned_transaction(ixs)

    def _cancel_order_ix(self, asset: Asset, order_id: int, side: Side) -> Instruction:
        if self._margin_account_address is None:
            raise Exception("Margin account address not loaded, cannot cancel order")
        if self._open_orders_addresses is None:
            raise Exception("Open orders addresses not loaded, cannot cancel order")
        return cancel_order(
            {"side": side.to_program_type(), "order_id": order_id, "asset": asset.to_program_type()},
            {
                "authority": self.provider.wallet.public_key,
                "cancel_accounts": {
                    "state": self.exchange._state_address,
                    "margin_account": self._margin_account_address,
                    "dex_program": constants.MATCHING_ENGINE_PID[self.network],
                    "serum_authority": self.exchange._serum_authority_address,
                    "open_orders": self._open_orders_addresses[asset],
                    "market": self.exchange.markets[asset].address,
                    "bids": self.exchange.markets[asset]._market_state.bids,
                    "asks": self.exchange.markets[asset]._market_state.asks,
                    "event_queue": self.exchange.markets[asset]._market_state.event_queue,
                },
            },
            self.exchange.program_id,
        )

    # TODO: cancelorderbyclientorderid

    def _cancel_orders_for_market_ix(self, asset: Asset) -> Instruction:
        if self._margin_account_address is None:
            raise Exception("Margin account address not loaded, cannot cancel orders")
        if self._open_orders_addresses is None:
            raise Exception("Open orders addresses not loaded, cannot cancel orders")
        return cancel_all_market_orders(
            {"asset": asset.to_program_type()},
            {
                "authority": self.provider.wallet.public_key,
                "cancel_accounts": {
                    "state": self.exchange._state_address,
                    "margin_account": self._margin_account_address,
                    "dex_program": constants.MATCHING_ENGINE_PID[self.network],
                    "serum_authority": self.exchange._serum_authority_address,
                    "open_orders": self._open_orders_addresses[asset],
                    "market": self.exchange.markets[asset].address,
                    "bids": self.exchange.markets[asset]._market_state.bids,
                    "asks": self.exchange.markets[asset]._market_state.asks,
                    "event_queue": self.exchange.markets[asset]._market_state.event_queue,
                },
            },
            self.exchange.program_id,
        )

    async def cancel_orders_for_market(self, asset: Asset):
        ixs = [self._cancel_orders_for_market_ix(asset)]
        self._logger.info(f"Cancelling all orders for {asset}")
        return await self._send_versioned_transaction(ixs)

    async def place_orders_for_market(
        self,
        asset: Asset,
        orders: list[OrderArgs],
        pre_instructions: list[Instruction] = None,
        post_instructions: list[Instruction] = None,
    ):
        ixs = []
        if not await self._check_open_orders_account_exists(asset):
            self._logger.info("User has no open orders account, creating one...")
            ixs.append(self._init_open_orders_ix(asset))

        if pre_instructions is not None:
            ixs.extend(pre_instructions)
        for order in orders:
            ixs.append(self._place_order_ix(asset, order.price, order.size, order.side, order.order_opts))
        if post_instructions is not None:
            ixs.extend(post_instructions)
        self._logger.info(f"Placing {len(orders)} orders for {asset}")
        return await self._send_versioned_transaction(ixs)

    async def replace_orders_for_market(
        self,
        asset: Asset,
        orders: list[OrderArgs],
    ):
        return await self.place_orders_for_market(
            asset, orders, pre_instructions=[self._cancel_orders_for_market_ix(asset)]
        )

    # TODO: liquidate
    async def liquidate(self):
        raise NotImplementedError

    async def _send_versioned_transaction(self, ixs: list[Instruction]):
        # TODO: prefetch blockhash (look into blockhash cache)
        recent_blockhash = (
            self.connection.blockhash_cache.get()
            if self.connection.blockhash_cache
            else (await self.connection.get_latest_blockhash(constants.BLOCKHASH_COMMITMENT)).value.blockhash
        )
        msg = MessageV0.try_compile(
            self.provider.wallet.public_key, ixs, [constants.ZETA_LUT[self.network]], recent_blockhash
        )
        tx = VersionedTransaction(msg, [self.provider.wallet.payer])
        try:
            signature = await self.provider.send(tx)
        except RPCException as exc:
            # This won't work on zDEX errors
            # TODO: add ZDEX error parsing
            parsed = from_tx_error(exc)
            self._logger.error(parsed)
            if parsed is not None:
                raise parsed from exc
            raise exc
        return signature

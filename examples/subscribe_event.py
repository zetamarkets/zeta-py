import asyncio
import os

import anchorpy
from anchorpy import EventParser
from solana.rpc.commitment import Confirmed
from solana.rpc.websocket_api import connect
from solders.rpc.config import RpcTransactionLogsFilterMentions

from zetamarkets_py.client import Client
from zetamarkets_py.events import (
    LiquidationEvent,
    OrderCompleteEvent,
    PlaceOrderEvent,
    TradeEvent,
)


async def main():
    # get local filesystem keypair wallet, defaults to ~/.config/solana/id.json
    wallet = anchorpy.Wallet.local()
    commitment = Confirmed
    endpoint = os.getenv("ENDPOINT", "https://api.mainnet-beta.solana.com")
    ws_endpoint = os.getenv("WS_ENDPOINT", "wss://api.mainnet-beta.solana.com")

    # load in client without any markets
    client = await Client.load(endpoint=endpoint, wallet=wallet, assets=[])

    # open up a websocket subscription
    async with connect(ws_endpoint) as ws:
        # subscribe to only logs/events that mention our margin account
        await ws.logs_subscribe(
            commitment=commitment, filter_=RpcTransactionLogsFilterMentions(client._margin_account_address)
        )
        first_resp = await ws.recv()
        first_resp[0].result
        print(f"Listening for events for margin account: {client._margin_account_address}")
        async for msg in ws:
            logs = msg[0].result.value.logs
            # parse log events based on the program coder
            parser = EventParser(client.exchange.program_id, client.exchange.program.coder)
            parsed = []
            parser.parse_logs(logs, lambda evt: parsed.append(evt))
            for event in parsed:
                # filter events to only those that are relevant to the user's margin account
                if event.name.startswith(PlaceOrderEvent.__name__):
                    if event.data.margin_account == client._margin_account_address:
                        print(PlaceOrderEvent.from_event(event))
                if event.name.startswith(OrderCompleteEvent.__name__):
                    if event.data.margin_account == client._margin_account_address:
                        print(OrderCompleteEvent.from_event(event))
                elif event.name.startswith(TradeEvent.__name__):
                    if event.data.margin_account == client._margin_account_address:
                        print(TradeEvent.from_event(event))
                elif event.name.startswith(LiquidationEvent.__name__):
                    if event.data.margin_account == client._margin_account_address:
                        print(LiquidationEvent.from_event(event))


asyncio.run(main())

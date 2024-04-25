import typing
from dataclasses import dataclass

import borsh_construct as borsh
from anchorpy.borsh_extension import BorshPubkey
from anchorpy.coder.accounts import ACCOUNT_DISCRIMINATOR_SIZE
from anchorpy.error import AccountInvalidDiscriminator
from anchorpy.utils.rpc import get_multiple_accounts
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment
from solders.pubkey import Pubkey

from .. import types
from ..program_id import PROGRAM_ID


class StateJSON(typing.TypedDict):
    admin: str
    state_nonce: int
    serum_nonce: int
    mint_auth_nonce: int
    num_underlyings: int
    num_flex_underlyings: int
    null: list[int]
    strike_initialization_threshold_seconds: int
    pricing_frequency_seconds: int
    liquidator_liquidation_percentage: int
    insurance_vault_liquidation_percentage: int
    deprecated_fee_values: list[int]
    native_deposit_limit: int
    expiration_threshold_seconds: int
    position_movement_fee_bps: int
    margin_concession_percentage: int
    treasury_wallet_nonce: int
    deprecated_option_fee_values: list[int]
    referrals_admin: str
    referrals_rewards_wallet_nonce: int
    max_perp_delta_age: int
    secondary_admin: str
    vault_nonce: int
    insurance_vault_nonce: int
    deprecated_total_insurance_vault_deposits: int
    native_withdraw_limit: int
    withdraw_limit_epoch_seconds: int
    native_open_interest_limit: int
    halt_states: list[types.halt_state_v2.HaltStateV2JSON]
    halt_states_padding: list[types.halt_state_v2.HaltStateV2JSON]
    trigger_admin: str
    min_lot_sizes: list[int]
    min_lot_sizes_padding: list[int]
    tick_sizes: list[int]
    tick_sizes_padding: list[int]
    deprecated_maker_fee_value: int
    native_take_trigger_order_fee_percentage: int
    native_maker_rebate_percentage: int
    ma_type_admin: str
    pricing_admin: str
    padding: list[int]


@dataclass
class State:
    discriminator: typing.ClassVar = b"\xd8\x92k^hK\xb6\xb1"
    layout: typing.ClassVar = borsh.CStruct(
        "admin" / BorshPubkey,
        "state_nonce" / borsh.U8,
        "serum_nonce" / borsh.U8,
        "mint_auth_nonce" / borsh.U8,
        "num_underlyings" / borsh.U8,
        "num_flex_underlyings" / borsh.U8,
        "null" / borsh.U8[7],
        "strike_initialization_threshold_seconds" / borsh.U32,
        "pricing_frequency_seconds" / borsh.U32,
        "liquidator_liquidation_percentage" / borsh.U32,
        "insurance_vault_liquidation_percentage" / borsh.U32,
        "deprecated_fee_values" / borsh.U64[3],
        "native_deposit_limit" / borsh.U64,
        "expiration_threshold_seconds" / borsh.U32,
        "position_movement_fee_bps" / borsh.U8,
        "margin_concession_percentage" / borsh.U8,
        "treasury_wallet_nonce" / borsh.U8,
        "deprecated_option_fee_values" / borsh.U64[2],
        "referrals_admin" / BorshPubkey,
        "referrals_rewards_wallet_nonce" / borsh.U8,
        "max_perp_delta_age" / borsh.U16,
        "secondary_admin" / BorshPubkey,
        "vault_nonce" / borsh.U8,
        "insurance_vault_nonce" / borsh.U8,
        "deprecated_total_insurance_vault_deposits" / borsh.U64,
        "native_withdraw_limit" / borsh.U64,
        "withdraw_limit_epoch_seconds" / borsh.U32,
        "native_open_interest_limit" / borsh.U64,
        "halt_states" / types.halt_state_v2.HaltStateV2.layout[15],
        "halt_states_padding" / types.halt_state_v2.HaltStateV2.layout[10],
        "trigger_admin" / BorshPubkey,
        "min_lot_sizes" / borsh.U32[15],
        "min_lot_sizes_padding" / borsh.U32[10],
        "tick_sizes" / borsh.U32[15],
        "tick_sizes_padding" / borsh.U32[10],
        "deprecated_maker_fee_value" / borsh.U64,
        "native_take_trigger_order_fee_percentage" / borsh.U64,
        "native_maker_rebate_percentage" / borsh.U64,
        "ma_type_admin" / BorshPubkey,
        "pricing_admin" / BorshPubkey,
        "padding" / borsh.U8[18],
    )
    admin: Pubkey
    state_nonce: int
    serum_nonce: int
    mint_auth_nonce: int
    num_underlyings: int
    num_flex_underlyings: int
    null: list[int]
    strike_initialization_threshold_seconds: int
    pricing_frequency_seconds: int
    liquidator_liquidation_percentage: int
    insurance_vault_liquidation_percentage: int
    deprecated_fee_values: list[int]
    native_deposit_limit: int
    expiration_threshold_seconds: int
    position_movement_fee_bps: int
    margin_concession_percentage: int
    treasury_wallet_nonce: int
    deprecated_option_fee_values: list[int]
    referrals_admin: Pubkey
    referrals_rewards_wallet_nonce: int
    max_perp_delta_age: int
    secondary_admin: Pubkey
    vault_nonce: int
    insurance_vault_nonce: int
    deprecated_total_insurance_vault_deposits: int
    native_withdraw_limit: int
    withdraw_limit_epoch_seconds: int
    native_open_interest_limit: int
    halt_states: list[types.halt_state_v2.HaltStateV2]
    halt_states_padding: list[types.halt_state_v2.HaltStateV2]
    trigger_admin: Pubkey
    min_lot_sizes: list[int]
    min_lot_sizes_padding: list[int]
    tick_sizes: list[int]
    tick_sizes_padding: list[int]
    deprecated_maker_fee_value: int
    native_take_trigger_order_fee_percentage: int
    native_maker_rebate_percentage: int
    ma_type_admin: Pubkey
    pricing_admin: Pubkey
    padding: list[int]

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: Pubkey,
        commitment: typing.Optional[Commitment] = None,
        program_id: Pubkey = PROGRAM_ID,
    ) -> typing.Optional["State"]:
        resp = await conn.get_account_info(address, commitment=commitment)
        info = resp.value
        if info is None:
            return None
        if info.owner != program_id:
            raise ValueError("Account does not belong to this program")
        bytes_data = info.data
        return cls.decode(bytes_data)

    @classmethod
    async def fetch_multiple(
        cls,
        conn: AsyncClient,
        addresses: list[Pubkey],
        commitment: typing.Optional[Commitment] = None,
        program_id: Pubkey = PROGRAM_ID,
    ) -> typing.List[typing.Optional["State"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["State"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "State":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator("The discriminator for this account is invalid")
        dec = State.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            admin=dec.admin,
            state_nonce=dec.state_nonce,
            serum_nonce=dec.serum_nonce,
            mint_auth_nonce=dec.mint_auth_nonce,
            num_underlyings=dec.num_underlyings,
            num_flex_underlyings=dec.num_flex_underlyings,
            null=dec.null,
            strike_initialization_threshold_seconds=dec.strike_initialization_threshold_seconds,
            pricing_frequency_seconds=dec.pricing_frequency_seconds,
            liquidator_liquidation_percentage=dec.liquidator_liquidation_percentage,
            insurance_vault_liquidation_percentage=dec.insurance_vault_liquidation_percentage,
            deprecated_fee_values=dec.deprecated_fee_values,
            native_deposit_limit=dec.native_deposit_limit,
            expiration_threshold_seconds=dec.expiration_threshold_seconds,
            position_movement_fee_bps=dec.position_movement_fee_bps,
            margin_concession_percentage=dec.margin_concession_percentage,
            treasury_wallet_nonce=dec.treasury_wallet_nonce,
            deprecated_option_fee_values=dec.deprecated_option_fee_values,
            referrals_admin=dec.referrals_admin,
            referrals_rewards_wallet_nonce=dec.referrals_rewards_wallet_nonce,
            max_perp_delta_age=dec.max_perp_delta_age,
            secondary_admin=dec.secondary_admin,
            vault_nonce=dec.vault_nonce,
            insurance_vault_nonce=dec.insurance_vault_nonce,
            deprecated_total_insurance_vault_deposits=dec.deprecated_total_insurance_vault_deposits,
            native_withdraw_limit=dec.native_withdraw_limit,
            withdraw_limit_epoch_seconds=dec.withdraw_limit_epoch_seconds,
            native_open_interest_limit=dec.native_open_interest_limit,
            halt_states=list(
                map(
                    lambda item: types.halt_state_v2.HaltStateV2.from_decoded(item),
                    dec.halt_states,
                )
            ),
            halt_states_padding=list(
                map(
                    lambda item: types.halt_state_v2.HaltStateV2.from_decoded(item),
                    dec.halt_states_padding,
                )
            ),
            trigger_admin=dec.trigger_admin,
            min_lot_sizes=dec.min_lot_sizes,
            min_lot_sizes_padding=dec.min_lot_sizes_padding,
            tick_sizes=dec.tick_sizes,
            tick_sizes_padding=dec.tick_sizes_padding,
            deprecated_maker_fee_value=dec.deprecated_maker_fee_value,
            native_take_trigger_order_fee_percentage=dec.native_take_trigger_order_fee_percentage,
            native_maker_rebate_percentage=dec.native_maker_rebate_percentage,
            ma_type_admin=dec.ma_type_admin,
            pricing_admin=dec.pricing_admin,
            padding=dec.padding,
        )

    def to_json(self) -> StateJSON:
        return {
            "admin": str(self.admin),
            "state_nonce": self.state_nonce,
            "serum_nonce": self.serum_nonce,
            "mint_auth_nonce": self.mint_auth_nonce,
            "num_underlyings": self.num_underlyings,
            "num_flex_underlyings": self.num_flex_underlyings,
            "null": self.null,
            "strike_initialization_threshold_seconds": self.strike_initialization_threshold_seconds,
            "pricing_frequency_seconds": self.pricing_frequency_seconds,
            "liquidator_liquidation_percentage": self.liquidator_liquidation_percentage,
            "insurance_vault_liquidation_percentage": self.insurance_vault_liquidation_percentage,
            "deprecated_fee_values": self.deprecated_fee_values,
            "native_deposit_limit": self.native_deposit_limit,
            "expiration_threshold_seconds": self.expiration_threshold_seconds,
            "position_movement_fee_bps": self.position_movement_fee_bps,
            "margin_concession_percentage": self.margin_concession_percentage,
            "treasury_wallet_nonce": self.treasury_wallet_nonce,
            "deprecated_option_fee_values": self.deprecated_option_fee_values,
            "referrals_admin": str(self.referrals_admin),
            "referrals_rewards_wallet_nonce": self.referrals_rewards_wallet_nonce,
            "max_perp_delta_age": self.max_perp_delta_age,
            "secondary_admin": str(self.secondary_admin),
            "vault_nonce": self.vault_nonce,
            "insurance_vault_nonce": self.insurance_vault_nonce,
            "deprecated_total_insurance_vault_deposits": self.deprecated_total_insurance_vault_deposits,
            "native_withdraw_limit": self.native_withdraw_limit,
            "withdraw_limit_epoch_seconds": self.withdraw_limit_epoch_seconds,
            "native_open_interest_limit": self.native_open_interest_limit,
            "halt_states": list(map(lambda item: item.to_json(), self.halt_states)),
            "halt_states_padding": list(map(lambda item: item.to_json(), self.halt_states_padding)),
            "trigger_admin": str(self.trigger_admin),
            "min_lot_sizes": self.min_lot_sizes,
            "min_lot_sizes_padding": self.min_lot_sizes_padding,
            "tick_sizes": self.tick_sizes,
            "tick_sizes_padding": self.tick_sizes_padding,
            "deprecated_maker_fee_value": self.deprecated_maker_fee_value,
            "native_take_trigger_order_fee_percentage": self.native_take_trigger_order_fee_percentage,
            "native_maker_rebate_percentage": self.native_maker_rebate_percentage,
            "ma_type_admin": str(self.ma_type_admin),
            "pricing_admin": str(self.pricing_admin),
            "padding": self.padding,
        }

    @classmethod
    def from_json(cls, obj: StateJSON) -> "State":
        return cls(
            admin=Pubkey.from_string(obj["admin"]),
            state_nonce=obj["state_nonce"],
            serum_nonce=obj["serum_nonce"],
            mint_auth_nonce=obj["mint_auth_nonce"],
            num_underlyings=obj["num_underlyings"],
            num_flex_underlyings=obj["num_flex_underlyings"],
            null=obj["null"],
            strike_initialization_threshold_seconds=obj["strike_initialization_threshold_seconds"],
            pricing_frequency_seconds=obj["pricing_frequency_seconds"],
            liquidator_liquidation_percentage=obj["liquidator_liquidation_percentage"],
            insurance_vault_liquidation_percentage=obj["insurance_vault_liquidation_percentage"],
            deprecated_fee_values=obj["deprecated_fee_values"],
            native_deposit_limit=obj["native_deposit_limit"],
            expiration_threshold_seconds=obj["expiration_threshold_seconds"],
            position_movement_fee_bps=obj["position_movement_fee_bps"],
            margin_concession_percentage=obj["margin_concession_percentage"],
            treasury_wallet_nonce=obj["treasury_wallet_nonce"],
            deprecated_option_fee_values=obj["deprecated_option_fee_values"],
            referrals_admin=Pubkey.from_string(obj["referrals_admin"]),
            referrals_rewards_wallet_nonce=obj["referrals_rewards_wallet_nonce"],
            max_perp_delta_age=obj["max_perp_delta_age"],
            secondary_admin=Pubkey.from_string(obj["secondary_admin"]),
            vault_nonce=obj["vault_nonce"],
            insurance_vault_nonce=obj["insurance_vault_nonce"],
            deprecated_total_insurance_vault_deposits=obj["deprecated_total_insurance_vault_deposits"],
            native_withdraw_limit=obj["native_withdraw_limit"],
            withdraw_limit_epoch_seconds=obj["withdraw_limit_epoch_seconds"],
            native_open_interest_limit=obj["native_open_interest_limit"],
            halt_states=list(
                map(
                    lambda item: types.halt_state_v2.HaltStateV2.from_json(item),
                    obj["halt_states"],
                )
            ),
            halt_states_padding=list(
                map(
                    lambda item: types.halt_state_v2.HaltStateV2.from_json(item),
                    obj["halt_states_padding"],
                )
            ),
            trigger_admin=Pubkey.from_string(obj["trigger_admin"]),
            min_lot_sizes=obj["min_lot_sizes"],
            min_lot_sizes_padding=obj["min_lot_sizes_padding"],
            tick_sizes=obj["tick_sizes"],
            tick_sizes_padding=obj["tick_sizes_padding"],
            deprecated_maker_fee_value=obj["deprecated_maker_fee_value"],
            native_take_trigger_order_fee_percentage=obj["native_take_trigger_order_fee_percentage"],
            native_maker_rebate_percentage=obj["native_maker_rebate_percentage"],
            ma_type_admin=Pubkey.from_string(obj["ma_type_admin"]),
            pricing_admin=Pubkey.from_string(obj["pricing_admin"]),
            padding=obj["padding"],
        )

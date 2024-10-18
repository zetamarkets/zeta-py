from solders.address_lookup_table_account import AddressLookupTableAccount
from solders.pubkey import Pubkey

from zetamarkets_py.types import Asset, Network

ZETA_PID = {
    # Network.LOCALNET: Pubkey.from_string("BG3oRikW8d16YjUEmX3ZxHm9SiJzrGtMhsSR8aCw1Cd7"),
    Network.DEVNET: Pubkey.from_string("BG3oRikW8d16YjUEmX3ZxHm9SiJzrGtMhsSR8aCw1Cd7"),
    Network.MAINNET: Pubkey.from_string("ZETAxsqBRek56DhiGXrn75yj2NHU3aYUnxvHXpkf3aD"),
}

MATCHING_ENGINE_PID = {
    # Network.LOCALNET: Pubkey.from_string("5CmWtUihvSrJpaUrpJ3H1jUa9DRjYz4v2xs6c3EgQWMf"),
    Network.DEVNET: Pubkey.from_string("5CmWtUihvSrJpaUrpJ3H1jUa9DRjYz4v2xs6c3EgQWMf"),
    Network.MAINNET: Pubkey.from_string("zDEXqXEG7gAyxb1Kg9mK5fPnUdENCGKzWrM21RMdWRq"),
}

# Asset keys are wormhole from mainnet.
MINTS = {
    Asset.SOL: Pubkey.from_string("So11111111111111111111111111111111111111112"),
    Asset.BTC: Pubkey.from_string("qfnqNqs3nCAHjnyCgLRDbBtq4p2MtHZxw8YjSyYhPoL"),
    Asset.ETH: Pubkey.from_string("FeGn77dhg1KXRRFeSwwMiykZnZPw5JXW6naf2aQgZDQf"),
    Asset.BNB: Pubkey.from_string("9gP2kCy3wA1ctvYWQk75guqXuHfrEomqydHLtcTCqiLa"),
}

# These are generated flexible PDAs and aren't reflective of an spl token mint.
FLEXIBLE_MINTS = {
    Network.DEVNET: {
        Asset.APT: Pubkey.from_string("FbfkphUHaAd7c27RqhzKBRAPX8T5AzFBH259sbGmNuvG"),
        Asset.ARB: Pubkey.from_string("w8h6r5ogLihfuWeCA1gs7boxNjzbwWeQbXMB3UATaC6"),
        Asset.PYTH: Pubkey.from_string("5PK1Ty2ac1Un6zY11Em7qF4FAYBgUu5y8Pt8ZtbepGnF"),
        Asset.TIA: Pubkey.from_string("3U2JttPo1k5xsapjuvQJQnH3Kj8D5HegF3PKoPReJ4JU"),
    },
    Network.MAINNET: {
        Asset.APT: Pubkey.from_string("8z8oShLky1PauW9hxv6AsjnricLqoK9MfmNZJDQNNNPr"),
        Asset.ARB: Pubkey.from_string("Ebd7aUFu3rtsZruCzTnG4tjBoxaJdWT8S3t4yC8hVpbo"),
        Asset.PYTH: Pubkey.from_string("BjZmtqBVKY1oUSUjgq9PBQWJPyWbcWTXYbQ1oWxa9NYp"),
        Asset.TIA: Pubkey.from_string("DmBnRoEiwGCud2C8X6h67ZLVhq6GyTm2NDRXvRz6uWYE"),
        Asset.JTO: Pubkey.from_string("71jxAnng6EMHYZzXEBoRZUnnhd8iyoAoc1soUgPDMt9e"),
        Asset.ONEMBONK: Pubkey.from_string("76x829V8cNWymEBNjUuE22bUcVnShNeRwnXnegviejyj"),
        Asset.SEI: Pubkey.from_string("CTw2xSSAfrv9hJGVpB2R2q5xYrdX79i3hXeCiQiAKf2f"),
        Asset.JUP: Pubkey.from_string("7uP5h7kxRaSbd2dz5e6gZp8yhqazyMvaXVoNZ4HsgZ2n"),
        Asset.DYM: Pubkey.from_string("FxxBzHfSZc794sRw6aLs7KuaG9iBy1hSLLFV8LLQYAiL"),
        Asset.STRK: Pubkey.from_string("C42HXAXQiV6EqxzTvmwff6FgCPNw7r2MgvJ9uv8UNdce"),
        Asset.WIF: Pubkey.from_string("7jCmRqJaJq5iojCwGqq5DdwUBYPhrpvJcgNZsFLM4Pd5"),
        Asset.RNDR: Pubkey.from_string("GSF4GTjWxacrQoVbf8PUcvCvMvZUzwXFEmb2Jso6XU5H"),
        Asset.TNSR: Pubkey.from_string("3bTWLSNoD95dP2SHq4diRz3ZTeDXmybTsjPUQzRpTCHR"),
        Asset.POPCAT: Pubkey.from_string("CoGwjBS8stc4HCwpa6xh55LmGRTPxPkNXDVc1qBjwa5"),
        Asset.EIGEN: Pubkey.from_string("F7pcDmpVokQJgToqN9DU7cmkWNgwUCd7qs3jZURMvL3L"),
        Asset.DBR: Pubkey.from_string("B69Kty2ejokBZQBGo4BUtQb1iAhjG2d8xTigL9PB4vRz"),
    },
}

PYTH_PRICE_FEEDS = {
    Network.DEVNET: {
        Asset.SOL: Pubkey.from_string("J83w4HKfqxwcq3BEMMkPFSppX3gqekLyLJBexebFVkix"),
        Asset.BTC: Pubkey.from_string("HovQMDrbAgAYPCmHVSrezcSmkMtXSSUsLDFANExrZh2J"),
        Asset.ETH: Pubkey.from_string("EdVCmQ9FSPcVe5YySXDPCRmc8aDQLKJ9xvYBMZPie1Vw"),
        Asset.APT: Pubkey.from_string("5d2QJ6u2NveZufmJ4noHja5EHs3Bv1DUMPLG5xfasSVs"),
        Asset.ARB: Pubkey.from_string("4mRGHzjGerQNWKXyQAmr9kWqb9saPPHKqo1xziXGQ5Dh"),
        Asset.BNB: Pubkey.from_string("GwzBgrXb4PG59zjce24SF2b9JXbLEjJJTBkmytuEZj1b"),
        Asset.PYTH: Pubkey.from_string("ELF78ZhSr8u4SCixA7YSpjdZHZoSNrAhcyysbavpC2kA"),
        Asset.TIA: Pubkey.from_string("4GiL1Y6u6JkPb7ckakzJgc414h6P7qoYnEKFcd1YtSB9"),
    },
    Network.MAINNET: {
        Asset.SOL: Pubkey.from_string("7UVimffxr9ow1uXYxsr4LHAcV58mLzhmwaeKvJ1pjLiE"),
        Asset.BTC: Pubkey.from_string("4cSM2e6rvbGQUFiJbqytoVMi5GgghSMr8LwVrT9VPSPo"),
        Asset.ETH: Pubkey.from_string("42amVS4KgzR9rA28tkVYqVXjq9Qa8dcZQMbH5EYFX6XC"),
        Asset.APT: Pubkey.from_string("9oR3Uh2zsp1CxLdsuFrg3QhY2eZ2e5eLjDgDfZ6oG2ev"),
        Asset.ARB: Pubkey.from_string("36XiLSLUq1trLrK5ApwWs6LvozCjyTVgpr2uSAF3trF1"),
        Asset.BNB: Pubkey.from_string("A3qp5QG9xGeJR1gexbW9b9eMMsMDLzx3rhud9SnNhwb4"),
        Asset.PYTH: Pubkey.from_string("8vjchtMuJNY4oFQdTi8yCe6mhCaNBFaUbktT482TpLPS"),
        Asset.TIA: Pubkey.from_string("6HpM5WSg4PCS4iAD13iSbcG4RbFErLS3pyC5qgtjqxqF"),
        Asset.JTO: Pubkey.from_string("7ajR2zA4MGMMTqRAVjghTKqPPn4kbrj3pYkAVRVwTGzP"),
        Asset.ONEMBONK: Pubkey.from_string("DBE3N8uNjhKPRHfANdwGvCZghWXyLPdqdSbEW2XFwBiX"),
        Asset.SEI: Pubkey.from_string("GATaRyQr7hq52GQWq3TsCditpNhkgq5ad4EM14JoRMLu"),
        Asset.JUP: Pubkey.from_string("7dbob1psH1iZBS7qPsm3Kwbf5DzSXK8Jyg31CTgTnxH5"),
        Asset.DYM: Pubkey.from_string("7RxdEbZV3ec7jfbUzVPucaDBY3KRY4FS797rmHHzYQSo"),
        Asset.STRK: Pubkey.from_string("CcRDwd4VYKq5pmUHHnzwujBZwTwfgE95UjjdoZW7qyEs"),
        Asset.WIF: Pubkey.from_string("6B23K3tkb51vLZA14jcEQVCA1pfHptzEHFA93V5dYwbT"),
        Asset.RNDR: Pubkey.from_string("GbgH1oen3Ne1RY4LwDgh8kEeA1KywHvs5x8zsx6uNV5M"),
        Asset.TNSR: Pubkey.from_string("9TSGDwcPQX4JpAvZbu2Wp5b68wSYkQvHCvfeBjYcCyC"),
        Asset.POPCAT: Pubkey.from_string("6UxPR2nXJNNM1nESVWGAf8NXMVu3SGgYf3ZfUFoGB9cs"),
        Asset.EIGEN: Pubkey.from_string("64x2TaUVMrmxGDCcWYntWR8TPrXA3uaC8TfX9997Kam"),
        Asset.DBR: Pubkey.from_string("5jdovW9tF9p4Wzd5SECyq8nE2ujgf5ZguqE8HHcHenw3"),
    },
}

USDC_MINT = {
    #   Network.LOCALNET: Pubkey.from_string("6PEh8n3p7BbCTykufbq1nSJYAZvUp6gSwEANAs1ZhsCX"),
    Network.DEVNET: Pubkey.from_string("6PEh8n3p7BbCTykufbq1nSJYAZvUp6gSwEANAs1ZhsCX"),
    Network.MAINNET: Pubkey.from_string("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"),
}

CHAINLINK_PID = Pubkey.from_string("HEvSKofvBgfaexv23kMabbYqxasxU3mQ4ibBMEmJWHny")

MAX_SETTLE_AND_CLOSE_PER_TX = 4
MAX_CANCELS_PER_TX = 3
MAX_CANCELS_PER_TX_LUT = 13
MAX_GREEK_UPDATES_PER_TX = 20
MAX_SETTLEMENT_ACCOUNTS = 20
MAX_FUNDING_ACCOUNTS = 20
MAX_REBALANCE_ACCOUNTS = 18
MAX_SETTLE_ACCOUNTS = 5
MAX_ZETA_GROUPS = 20
MAX_MARGIN_AND_SPREAD_ACCOUNTS = 20
MAX_SET_REFERRALS_REWARDS_ACCOUNTS = 12
MAX_INITIALIZE_MARKET_TIF_EPOCH_CYCLE_IXS_PER_TX = 15
MARKET_INDEX_LIMIT = 19
MARKET_LOAD_LIMIT = 12
MAX_MARKETS_TO_FETCH = 50

MIN_NATIVE_MIN_LOT_SIZE = 1
MIN_NATIVE_TICK_SIZE = 100

PERP_MARKET_ORDER_SPOT_SLIPPAGE = 0.02

# This is the most we can load per iteration without
# hitting the rate limit.
MARKET_LOAD_LIMIT = 12

# Numbers represented in BN are generally fixed point integers with precision of 6.
PLATFORM_PRECISION = 6
MARGIN_PRECISION = 8
POSITION_PRECISION = 3

DEFAULT_ORDER_TAG = "SDK"

MAX_POSITION_MOVEMENTS = 10
BPS_DENOMINATOR = 10_000

DEFAULT_MICRO_LAMPORTS_PER_CU_FEE = 1000

# DEX
BASE_MINT_DECIMALS = 0
QUOTE_MINT_DECIMALS = 6

ZETA_LUT = {
    # Network.LOCALNET: None,
    Network.DEVNET: AddressLookupTableAccount(
        key=Pubkey.from_string("2ea7yKr6Z86SVrhmnujBHGuiWnxFPb6YjzM3SG2FNhW4"),
        addresses=[
            Pubkey.from_string("9VddCF6iEyZbjkCQ4g8VJpjEtuLsgmvRCc6LQwAvXigC"),
            Pubkey.from_string("BditorsEXbVw6R8Woe6JhoyXC1beJCixYt57UMKuiwQi"),
            Pubkey.from_string("5CmWtUihvSrJpaUrpJ3H1jUa9DRjYz4v2xs6c3EgQWMf"),
            Pubkey.from_string("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"),
            Pubkey.from_string("7m134nU79ezr3b7jYSehnhto94AvSP4yexa3Wdhxff99"),
            Pubkey.from_string("SysvarRent111111111111111111111111111111111"),
            Pubkey.from_string("HEvSKofvBgfaexv23kMabbYqxasxU3mQ4ibBMEmJWHny"),
            Pubkey.from_string("J83w4HKfqxwcq3BEMMkPFSppX3gqekLyLJBexebFVkix"),
            Pubkey.from_string("99B2bTijsU6f1GCT73HmdR7HCFFjGMBcPZY6jZ96ynrR"),
            Pubkey.from_string("HovQMDrbAgAYPCmHVSrezcSmkMtXSSUsLDFANExrZh2J"),
            Pubkey.from_string("6PxBx93S8x3tno1TsFZwT5VqP8drrRCbCXygEXYNkFJe"),
            Pubkey.from_string("EdVCmQ9FSPcVe5YySXDPCRmc8aDQLKJ9xvYBMZPie1Vw"),
            Pubkey.from_string("669U43LNHx7LsVj95uYksnhXUfWKDsdzVqev3V4Jpw3P"),
            Pubkey.from_string("5d2QJ6u2NveZufmJ4noHja5EHs3Bv1DUMPLG5xfasSVs"),
            Pubkey.from_string("11111111111111111111111111111111"),
            Pubkey.from_string("5SSkXsEKQepHHAewytPVwdej4epN1nxgLVM84L4KXgy7"),
            Pubkey.from_string("11111111111111111111111111111111"),
            Pubkey.from_string("GwzBgrXb4PG59zjce24SF2b9JXbLEjJJTBkmytuEZj1b"),
            Pubkey.from_string("11111111111111111111111111111111"),
            Pubkey.from_string("ELF78ZhSr8u4SCixA7YSpjdZHZoSNrAhcyysbavpC2kA"),
            Pubkey.from_string("AVQutgTg4Jd4o4A4P4aYLJF3gpq7xmsE6DZqw1Eq2NvS"),
            Pubkey.from_string("JB43m9cTZVb4LcEfBA1Bf49nz4cod2Xt5i2HRAAMQvdo"),
            Pubkey.from_string("6YcgjoTUTeafyFC5C6vgFCVoM69qgpj966PhCojwiS4Z"),
            Pubkey.from_string("qjoUa8fC1DjsnwVwUCJQcVDJVYUhAnrqz3B9FSxVPAm"),
            Pubkey.from_string("5kSQn4o4S4mRR48sLZ5kijvCjnnD4NbwPqaBaQYvC6wk"),
            Pubkey.from_string("7Nm1pAysuk38D6uiU83wXfegzruqohVNwUippwSZNx71"),
            Pubkey.from_string("V6Y9bCVTTwjBDYAJ6ixMWWFK7RKZcQeUcpufZaM3DDB"),
            Pubkey.from_string("5yiNVYs4xpC26yY9K3DYTRvdFkdjBSnkyeSAA3Huf4Q2"),
            Pubkey.from_string("CjwQEszLimhf3FkwqcB5rGppZS4ADLeCmtPvcRefv5qi"),
            Pubkey.from_string("HM95yakZehLhBkVx2a5mwzTTf4UeqfDeSno17NstQKzd"),
            Pubkey.from_string("GHSuFYv8SicmVC3c5DeKgFhjDdegNH552srPFufFysDU"),
            Pubkey.from_string("HT9nmiVtAbLp3GFtfrhGCPGz1tBcvHyFz43pf8rtDArs"),
            Pubkey.from_string("J8yPaachUYRo1qbtdvkQU6Ee2vzEt3JiYRncwkfoB3iZ"),
            Pubkey.from_string("D9mSSsfXp9SUrSCrmPA8sDJ42GMn65Z5tZr9wtwbHEBy"),
            Pubkey.from_string("AYUthyJDg6mvBWjGfEGYcnjRbw3TZbYCnEQyqUiPyw57"),
            Pubkey.from_string("D7g6CGNVzebzzH1t98tBJKjA6FokiuXKaX3QVF53ZqcC"),
            Pubkey.from_string("DLzvYrHo4bT8PoSwhxDWKhH9ZNsnPbE5cgCx1coCpeR6"),
            Pubkey.from_string("2CtvLehungAsAcYhqnhLEoxuTaM5WqHrycn2YNpmnC4z"),
            Pubkey.from_string("9bGCvH7MwfwyKuNzgfGRXU8sW9jWtFMJf4FmUsQxk13Z"),
            Pubkey.from_string("8pQvXjUf9qq6Lsk9WE8tqtPXxgf4Yav32DneQDLaJr9k"),
            Pubkey.from_string("Gxc3KYEgasnSbevj9GnzwDk2i82BRHACQ8HWtgA1VXUk"),
            Pubkey.from_string("2fgyaTU1BeSk3LWbEh9p3D1H29hEt1wyy8qchKNGxBhg"),
            Pubkey.from_string("FDXX8a9asz32d6EteL6Wnra71YjT45TuGHy8Y8dPntbq"),
            Pubkey.from_string("JCk2bU5xNDUBk55W5BoEgNeKqssXdj15vLqhuzQEEiCU"),
            Pubkey.from_string("HYv5Vb7G3849dYN8RG2pQx7awXiEk3nE9F3AGWnedffs"),
            Pubkey.from_string("5RDbC6wYGhc1AjCCArwggtbAyPUse6yMcq3fgSzZqY5E"),
            Pubkey.from_string("2CCypxRdB6tCackur4De72ZSnsNcicfSjWYZwAcVzEZ9"),
            Pubkey.from_string("J5e19jEz625k7K5K3yinpMoHNzznv8smCemvKAYCWLMH"),
            Pubkey.from_string("7QDHQhNjMzuKKk9T5vsdZ5hTfLu2P1pUGk2TKJKFd8hn"),
            Pubkey.from_string("DYXqC6UGPwsz5W3jaFAJtpbBsvJpBSi34W6cMn7ZiL6m"),
            Pubkey.from_string("2YBnvgCAh6WcXrs5Wz2uhi2nMuEVDXE28mQ5AmHjRaJQ"),
            Pubkey.from_string("wkTZtYAo75bpqqy2J5A6emsLK69EYG8otvJipAbiJF9"),
            Pubkey.from_string("FXgqEhVGX82dsyKMAgR2JCRaC9FNH4ih611bJftmD3tG"),
            Pubkey.from_string("B3iV7Y5S9Xqu6cTECpBCAHtL2nwvZntD2d7F1zbpbQc3"),
            Pubkey.from_string("J7E7gv1iofWZg8b37RVnKy2i1FAnCRBvgk54YpVtZ4WS"),
            Pubkey.from_string("EPf7hymYW7bnwiBYGTRF4Ji2jJ2yTdn4XMTpR6N4zsGA"),
            Pubkey.from_string("DNXXx5yaQm6Kd4embzqHW94kjjypxzZ8zCQthMvmHDq1"),
            Pubkey.from_string("6VUvm4i9T2w9CXzLKaUDNTZ4KmK3xKCWz95xEoyKjjE8"),
            Pubkey.from_string("Dd3K16uKGDa2Xc83NYQE9jpcMNZ9GRqmqggkkpXo4x4y"),
            Pubkey.from_string("FUsWmTk7PaEvXCHFZH6XMbimgqbVkiKPXd35tHWo5vm4"),
            Pubkey.from_string("Fc7FU4VATyYuvkhp6MuPUHWYHC9EBFknN5TTHs3wGjyn"),
            Pubkey.from_string("CW5zwzmhQn9Pqjzxjdzr4AdmVSoehBQ2RdfyppU37uDE"),
            Pubkey.from_string("Cvqd7RtB4bf9SJpmWwNd6GVXvtAX4m4DtSR5u2XahTQf"),
            Pubkey.from_string("67XFnD7YuBfd52qPrD5FuasrQW21jLd4jxnDfozyeSvx"),
            Pubkey.from_string("3H7nvQAJBzsXVPEyzpuL4kB3tPz5rs7XVxuxVLV7YDNy"),
            Pubkey.from_string("JEDqstU8skdUF6bGsMzZaa17Tfuf3asxQPuLVXqmWqyt"),
            Pubkey.from_string("2Ux9NzgadfR2PHyrSauzWLaNr99syCRKriwF4mnEqPUv"),
            Pubkey.from_string("4NEK9db8v9PZC5RnzSEh596jNwfRMH6QcQQG2ZhqkStb"),
            Pubkey.from_string("2mRZPMv67hz1QocPQ7JS5sEp8uD9u9TfdLoZzf8LciiZ"),
            Pubkey.from_string("G3ytGgn7MzH5DpLCSBshkV4xQe1G4JBbTu7c9CCWA9U"),
            Pubkey.from_string("J5t2VsFLSXGTaA1o2qCujduJ9dnHLok9QhYUroN2fc6X"),
            Pubkey.from_string("6UEwXk5ixtC6rDJG7X2X6MLNwiAyjGZZyN6L1JG63n4H"),
            Pubkey.from_string("FkHx7byyFDGheXCcmVxdavTDteotaDJZk8DBNBm2Maeb"),
            Pubkey.from_string("zXEzviQpq8u89oAKdU7r3vHHxXpxC2547AoLzxCKSJ3"),
            Pubkey.from_string("93DGPpMR6w3gqbrbpZrChqw8vihgHibmdejB4Q1p4DbP"),
            Pubkey.from_string("Ag4cqXXAAxa9NCZcFgQuoeDkvtSbxwe6qaEfjw4aRnUH"),
            Pubkey.from_string("2j1BJUDD9dXXzypVyjT5HXAy1e11VzjtMpGW4U7ynJXP"),
            Pubkey.from_string("BN7EMGBdTBkJfAtuRhUWpDdewqk6RVF2CvyVku6fvH26"),
            Pubkey.from_string("8yNLGd4fngCtsXeoVoEEE22Bicjkcuvq9GWbdHd6b6nK"),
            Pubkey.from_string("HaAPQFP2nxinog4SDzJ8pZCv7eFNXxCxzhQrm5JrHckq"),
            Pubkey.from_string("GQH1eMDvw9hysVFiiVRwdjWW4Pow5AjguY3U39Gnn1my"),
            Pubkey.from_string("5xAbQKS8qdS4D5h78AusSraZDqyPjGfiDyzQNRBSgyqD"),
            Pubkey.from_string("DwvnBtJW1x8LANmaVPgUt8F9uY9AEnXH9CM1dsBxvpd7"),
            Pubkey.from_string("Ch4Gd1tyNhGnqRrHD112PvgevmCi5RA8br4CRESdJp9R"),
            Pubkey.from_string("D2MvxY79gJUs1b1VmEiDTN85r8vgQDxU9Z2vE5oKVa4N"),
            Pubkey.from_string("6KjVaBHGvFGcVzptCmqUgE6mRnLrbtssSP2nVN4SJWw8"),
            Pubkey.from_string("DZP6WX2p8ZERhr9qHxpySt3hR77KU38KLFth1JfAhGe4"),
            Pubkey.from_string("AVQutgTg4Jd4o4A4P4aYLJF3gpq7xmsE6DZqw1Eq2NvS"),
            Pubkey.from_string("7pbGP7MoJZ7zpr5ngWrURjDMk3dgxdphnnURot7V2Nvs"),
            Pubkey.from_string("6f35vNsWmky1wkiMGcXk7KUZUszaAfmBNv4tod9ZguXD"),
            Pubkey.from_string("7edomgWHCcwR8rG349wWZDCVXba9BZxon5LcEnnx4kow"),
            Pubkey.from_string("FJBabair8yvFbuYFaDK8Neqjof1BbWPS3wjpR17sKkst"),
            Pubkey.from_string("C5oGeBgUREHZzHXjPbLLiBRBe6w6G91LYHjejQHAA6qL"),
            Pubkey.from_string("8vrZSqsXrzMtR53iCrwVgh4bVh1LYANW2xQ5qZoQH3kw"),
            Pubkey.from_string("5ub4h28b5d8Muf4Cw8JzET7BzCYe3vUALqXWedbzwuNG"),
            Pubkey.from_string("2DWDgtCYtVvV6fpN9WHhMztt4fWgNcdpn5hGVcXWxe6Z"),
            Pubkey.from_string("7Ty1AkSCmHpMLFNjH7xW2s2DkcMWggg3MkyYfWmwcKa5"),
            Pubkey.from_string("DS4ThY5eeu7orkMbueVW2zwQVG8FUhBGn1dm1WyxH75P"),
        ],
    ),
    Network.MAINNET: AddressLookupTableAccount(
        key=Pubkey.from_string("6JCasgqNjup9pDuoHL7ymHFaGUHrWbF3VFggHaHuGyes"),
        addresses=[
            Pubkey.from_string("8eExPiLp47xbSDYkbuem4qnLUpbLTfZBeFuEJoh6EUr2"),
            Pubkey.from_string("BbKFezrmKD83PeVh74958MzgFAue1pZptipSNLz5ccpk"),
            Pubkey.from_string("zDEXqXEG7gAyxb1Kg9mK5fPnUdENCGKzWrM21RMdWRq"),
            Pubkey.from_string("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"),
            Pubkey.from_string("AVNMK6wiGfppdQNg9WKfMRBXefDPGZFh2f3o1fRbgN8n"),
            Pubkey.from_string("SysvarRent111111111111111111111111111111111"),
            Pubkey.from_string("7UVimffxr9ow1uXYxsr4LHAcV58mLzhmwaeKvJ1pjLiE"),
            Pubkey.from_string("JE6d41JRokZAMUEAznV8JP4h7i6Ain6CyJrQuweRipFU"),
            Pubkey.from_string("EaNR74nCjrYyNDsuoWmq19pH76QSd1nuTzvJSr3RDQ6x"),
            Pubkey.from_string("3rjBffJkFa9zdGr9xmTVxF3y6nL6iL1pASVzym7s5FGr"),
            Pubkey.from_string("HcjrQKnbqKJuxHDLNM9LJPyxcQs237waNZXW7RwgvAps"),
            Pubkey.from_string("Ec4xsLLgLc4wM5c19ZSvazE7M9Rtk2T6RzddNcSQKYGu"),
            Pubkey.from_string("BEjGhNFnKT5weGtpBoFs5Y1mDN47Ntvag5aMV59nZRpk"),
            Pubkey.from_string("CHBUBfU3zscTNsihdK3x44TbpTza1hwcsTUaZfk751b5"),
            Pubkey.from_string("GYm6qTFwkGJx2ywetEuYrjHjhzVFCM2TwayyqS1HUPLG"),
            Pubkey.from_string("7aXkF7AZE2D3h128eNJ7VVp72HCV1izjKFsJ8uNWtCFN"),
            Pubkey.from_string("BKt2FdgBahn77joeawhNidswFxfgasPYCHWghRL4AKBR"),
            Pubkey.from_string("2ZLdhFsrkAtdn9Kud4SZvqchQFvn5jVCHUdJ83vumKyR"),
            Pubkey.from_string("4cSM2e6rvbGQUFiJbqytoVMi5GgghSMr8LwVrT9VPSPo"),
            Pubkey.from_string("J5DTCqRAjX1FyzoP2A2HVmmaXuG971HJ8X1Z8Rvvd8uT"),
            Pubkey.from_string("6JSdqUr24mBt4MCQrZHRoSfeZbjgALx4MQunZwD8Uarg"),
            Pubkey.from_string("4K1zxqAZn7bGAPN26W5mUaHrLMSpCk45gT4qVXwmfh39"),
            Pubkey.from_string("8JSbFw4YT3bzpbbHs1wKmRCSAmKucAba7XSUWj1p8xK5"),
            Pubkey.from_string("483SmqGQVxw3WDwcewMYHqC3Mu7ENxfTQJQtTR3ttpi7"),
            Pubkey.from_string("DbzL5mT4nBaxuAs8ti4UeT2qougRBdujxa7GhLndM5Jz"),
            Pubkey.from_string("7M9xhY2ARnrkCaBK5SNM3Lyd3FdbTu2EWBwG4TQcqpsv"),
            Pubkey.from_string("5mvaZWcZa4gB3JZptZuFAJnmDFfo1JovhqTkkfEcsryD"),
            Pubkey.from_string("DboTtkWW3KPvT14fag8N6iDUyDXaT8FeBszGV9xdfBx2"),
            Pubkey.from_string("DhMH8oRQoAAb6poHVsvCqq3NCMj6aKUH2tGQG5Lo4bCg"),
            Pubkey.from_string("63DZkAzoDXmzGzn9esoWSYpMLo4YB9oPHXreHKwuu4HA"),
            Pubkey.from_string("42amVS4KgzR9rA28tkVYqVXjq9Qa8dcZQMbH5EYFX6XC"),
            Pubkey.from_string("J8x6y5G7GmTkuKTbbCAnfhn72vaUU2qsB6je9oKFigHM"),
            Pubkey.from_string("A7D8zuxAmtui3XKz2VcxthAZ5HuwLbN74rrDapMJ3Z5d"),
            Pubkey.from_string("CzK26LWpoU9UjSrZkVu97oZj63abJrNv1zp9Hy2zZdy5"),
            Pubkey.from_string("CaqN8gomPEB1My2czRhetrj5ESKP3VRR3kwKhXtGxohG"),
            Pubkey.from_string("4oAjuVLt5N9au2X3bhYLSi9LRqtk4caBvSPQRwhXuEKP"),
            Pubkey.from_string("9YVE9r9cHFZNwm91p3Js8NBWVznesLSM8FZyswG2MG1B"),
            Pubkey.from_string("DecjLCYjb7jdDp2UqA2MS4xjgDjZfvdgMjvkRW7oWs9L"),
            Pubkey.from_string("8SH6uJe5rV13APZFQvkGdXPwTyeiLv67XTnv3EeYff3B"),
            Pubkey.from_string("DhWWXYK2DSnCdK5rkAxJBkGb1SBR49RHpfHj2u1vobCJ"),
            Pubkey.from_string("5Ehp2LtTRmjug39GphXhFEeguz7hGeg41N1U49wU8Kov"),
            Pubkey.from_string("2Stzi7XE3btUQXaauTVB9brPAtPmGnrEDSJmp3w5VY2j"),
            Pubkey.from_string("9oR3Uh2zsp1CxLdsuFrg3QhY2eZ2e5eLjDgDfZ6oG2ev"),
            Pubkey.from_string("J6feTwcYDydW71Dp9qgfW7Mu9qk3qDRrDZAWV8NMVh9x"),
            Pubkey.from_string("EPf7hymYW7bnwiBYGTRF4Ji2jJ2yTdn4XMTpR6N4zsGA"),
            Pubkey.from_string("DNXXx5yaQm6Kd4embzqHW94kjjypxzZ8zCQthMvmHDq1"),
            Pubkey.from_string("6VUvm4i9T2w9CXzLKaUDNTZ4KmK3xKCWz95xEoyKjjE8"),
            Pubkey.from_string("Dd3K16uKGDa2Xc83NYQE9jpcMNZ9GRqmqggkkpXo4x4y"),
            Pubkey.from_string("GqCVQuGMf8YkiaJkSrD98D3WZxFfktcKzAwdBEQsx1th"),
            Pubkey.from_string("2BpEtArGNotp97DjVKwhYZ86WEq2Y5bLtGGDvicuJ9br"),
            Pubkey.from_string("6nkbQueQanrsg2JVvqoZ6zPuZsiL3oLmTk7xgEpRAirD"),
            Pubkey.from_string("7T1qeETZ6ZpbKJ7wmrWoxhewLaJRW9H4EgMnR1tgHYRQ"),
            Pubkey.from_string("6S6WYL1mQFmVxsf3ft5MEH8hzxJA1LcUDzgwdJDj3yxc"),
            Pubkey.from_string("GuNWJSV4k95FZdwhAcjdaPGGoh9cArc27yV4P54QwWdg"),
            Pubkey.from_string("36XiLSLUq1trLrK5ApwWs6LvozCjyTVgpr2uSAF3trF1"),
            Pubkey.from_string("J18LXTGe2cPgpLKSCwXiG6tYkjcqEiaMUznM19Q8faVL"),
            Pubkey.from_string("gP91avgCrV9KB2ATgRtMCNN2AN7oU9hK1frENe17QkR"),
            Pubkey.from_string("DUtwwtnNBzpPTnzUiz23vqH93gd1qwEzGisyC5bLwCBv"),
            Pubkey.from_string("A4SayHehmafd6DNjrzY3L9ddQEGw4UHV3LMcKfmyPcMT"),
            Pubkey.from_string("8if1NcDaif8dxM3Ct6rRTQEj9GFwukadU1MDQHqCnw9h"),
            Pubkey.from_string("GnSRgncxFbtxqZ4HmfnF6daCmgkc8tuQz9i37hUmwV5t"),
            Pubkey.from_string("6JjDgGzqzU6Az7ZmTARAvBSwBxfXsqbVG3Rc9JGU9i4L"),
            Pubkey.from_string("GQXdvh4dHvENTFi2CfVrh77aQD1Y6V7HMNYNCuvgbSuc"),
            Pubkey.from_string("EC2PCjwcuBBFHp6gpAKa3kdpLVrQxdy7kgr7p4wPy8Vw"),
            Pubkey.from_string("7j1N5UiXLFxaxFWq5tzZc5R3sjPHcF7jqfHJgAtE74q8"),
            Pubkey.from_string("Eqt3anUy8nqDvzJaNvWvqBM32Ln4UUnLkfvdd9Ztfj81"),
            Pubkey.from_string("A3qp5QG9xGeJR1gexbW9b9eMMsMDLzx3rhud9SnNhwb4"),
            Pubkey.from_string("6C3K3LDgVeiKZ93d4TTsax6qxjmr2Hm61873aR8ykJYT"),
            Pubkey.from_string("Ao4fdNfwP1KPUwxoKbKVZ3Jp12MiCsK8gvvxbumn75by"),
            Pubkey.from_string("238aPEmvSnFdra3gMYz2NPSwHPPTaf5bGxaqMXMs35GE"),
            Pubkey.from_string("5JLWHAW2fX7C2PFc2Len3kUfjYJAKLAyUhb8i9nr9cH3"),
            Pubkey.from_string("HhcUi31CHLScAV1dpQq1suxsXpg331fETUZU1GsNgVSx"),
            Pubkey.from_string("GNp5Q8fwD45azybdXKfuYYTHRkUh2krX9ejYuNKMFNmR"),
            Pubkey.from_string("DZdqa3nVJmyPc2ei397Cr1TufzZiNG3G6aRrV1AZ52p7"),
            Pubkey.from_string("5qxoTJ3N5GRNJnWuZ4E8Ak4MUB4hiPwyCrn3VMPmgsAM"),
            Pubkey.from_string("3cU8siJiNomBZDB12qA5QoRTwUMi2ZUa6f496js2RUwf"),
            Pubkey.from_string("5DPKMXmf9WK1C6N1MoJLWjYApiP4KR8zNf1oofevGEub"),
            Pubkey.from_string("B6sV248kSsj6n72osn3Wcuz87JX3RFMD7FZpgwdYGQTm"),
            Pubkey.from_string("8vjchtMuJNY4oFQdTi8yCe6mhCaNBFaUbktT482TpLPS"),
            Pubkey.from_string("ALYccFbb6ZPmUuiGeFC6pers4bfgpV2RtKoFiAsyQK8X"),
            Pubkey.from_string("DCSXWke6HzdA8J6FhcxxM7mrdr4mkNhN32KjVAPtCZeG"),
            Pubkey.from_string("8tjRWGXkCAszLS1XF5Vf7uEiGvhpggaG2aNmqcvuKUC8"),
            Pubkey.from_string("8jU96TshKzrLqXzZbUL5privTaT6RQqV1rGeJ6EMuoYS"),
            Pubkey.from_string("D9A4dFKehqpcyNDdeRYvA9hkUDa2RUTF7zN6vwZVnT6w"),
            Pubkey.from_string("7cdY8U9Q5T5ktvF8VtkkZ1E7bt5mqbcQJQUw4433uEaV"),
            Pubkey.from_string("137rR2TJ7ryu7nBxNNCeCdXqEt79jQLo4YvTzhEoAEh4"),
            Pubkey.from_string("4LhMuCufFL4aR1UvnNQ4zP49FqmjRj4uVrJ9qE7L1GxS"),
            Pubkey.from_string("8UxG6sugH55rMybJkVXt3Pb3pJh9ZfRQbzajHEDDezsT"),
            Pubkey.from_string("7Pnbf6WLGpsYjbjnQN4t8wMCzdDGsx9ZAyuLd4vZmN49"),
            Pubkey.from_string("5Q245C352ChdBGWmNbiYmFneAUiMjhnbPwUqmdHWJ8U6"),
            Pubkey.from_string("6HpM5WSg4PCS4iAD13iSbcG4RbFErLS3pyC5qgtjqxqF"),
            Pubkey.from_string("EgN8rGcr2DRokxCebhkXuGBAQVkGeq7mGmzCGXsviT8r"),
            Pubkey.from_string("6xkyhooKT2wnciP7xjipque9SDwHwPPamwsprsoVXgg9"),
            Pubkey.from_string("FV8EEHjJvDUD8Kkp1DcomTatZBA81Z6C5AhmvyUwvEAh"),
            Pubkey.from_string("7qPuwhidbrkuVPEKSzKTCJdTgK5sfNLRGjfNkDqiLvPi"),
            Pubkey.from_string("3GxVoZpmiKLhDRa2cfVvDkbtVakm2f6sdW2TkDXMVsPt"),
            Pubkey.from_string("CXWkPH6BzU8dhNy3LQkaCH54jSxQATyp11wHuhsAzT9n"),
            Pubkey.from_string("2x1c7fXQdL5TDK9jbMvJ5VYM7wmPKUAQXrLAAFjvxSoc"),
            Pubkey.from_string("EJ2oxzqG3uKmD8FrbBRevQpZrvcQMRFA2fYauChcihaK"),
            Pubkey.from_string("BuDP4G7gjs4KdSQf1QenAygF8FksjH5Wu57maC9sezq7"),
            Pubkey.from_string("JB7F3kQvRYcQj8kogwGR78CMshg857E96ef4LQYDzSu1"),
            Pubkey.from_string("Bm6PXLobn7LBudgNdJKzUUNumAKAnEWuCoLVafsvPBda"),
            Pubkey.from_string("7ajR2zA4MGMMTqRAVjghTKqPPn4kbrj3pYkAVRVwTGzP"),
            Pubkey.from_string("FPia9JqQZ6XBe3Kq9MA4bbFaqojiSNePLbVLQj7hKqqa"),
            Pubkey.from_string("9uYZdYf8aQd9YK6UrGUmz78pYpHscgHdD5f4cZojvmpH"),
            Pubkey.from_string("7HzkSBwxFTft413SFQoznSpd9zu8yWLoPc51QY9Y2Uwb"),
            Pubkey.from_string("9zGXeYAtgaMSafxCQxCTCWnK7W76wbPbjTYeMrCKx3wh"),
            Pubkey.from_string("FCZjBQniB2WJjQhk2DR4kYvsoy7fj9PCKqyU6j3uQ8rx"),
            Pubkey.from_string("2BXEjZqnRBhj3BrRbMERWnToEKErzxZmLPzLEmBHKdJT"),
            Pubkey.from_string("9g3YcLnENdQKYCxg88o1VUhSXJQVD3Kf7uMVB7d1SyuG"),
            Pubkey.from_string("3Vxn3hUebS9wYo5ejbhrXtxjDpp8iko4TW7sj3ub5wmv"),
            Pubkey.from_string("BaiBruf847DKccBnGtfNgMm6mjHeXoYs64ZoFK5uuV6Z"),
            Pubkey.from_string("GZycSPLqxhZuQYmv5wWjdwK4v3T1WStBpGxYem691vMG"),
            Pubkey.from_string("Avy1abPkJKJdadFVieTuF8oeN6ZFWsKNtKzU1a8tgn6Z"),
            Pubkey.from_string("DBE3N8uNjhKPRHfANdwGvCZghWXyLPdqdSbEW2XFwBiX"),
            Pubkey.from_string("Dy7j5mY3nxud8bow34MBUPhZqXutJRPjzEiXyNeiSMdD"),
            Pubkey.from_string("CgUMT14wR6WHX9mKMS5BWtd4tk39hRxbxtNRvp4BdMHf"),
            Pubkey.from_string("5Kdbu8k9hPU8fhAcszN2HYZdq5MHspV3y9ZKHA3t39ko"),
            Pubkey.from_string("4EVR1QadXD8SQeEnzkVv2BUfJaYoM7iPcGziiuAgWPhi"),
            Pubkey.from_string("CSh9paLCAfvE853RYQUtkCLqtBao87RX9FcxirK3pdX7"),
            Pubkey.from_string("gn46ys7QKtWqQAW2MsuSV475AcFGn7gdNnSCLgw71DL"),
            Pubkey.from_string("HTN3dEduTUp2VuFgo885BJ3KTp8WrPrZgEPiCVg2cVtD"),
            Pubkey.from_string("JDRP3wxczYJ265fGUKXc26ZuDaHgp12CnSbPupsRvQUT"),
            Pubkey.from_string("ETUAXwjeEEprVToJbMzB3vBJfLpEPxKzexdgmkMXuEk7"),
            Pubkey.from_string("J7yjhCLdftzL95kGetry8pyX4eXn4Tjjh7KoWo599Sry"),
            Pubkey.from_string("GdAX1L7jNsMmfN3kcCijk774aE2UtARV8frTozeUWT2E"),
            Pubkey.from_string("GATaRyQr7hq52GQWq3TsCditpNhkgq5ad4EM14JoRMLu"),
            Pubkey.from_string("5h5WtXRW6Hy5s846DU8GSPgoDgnxKFUFK3mYiEy9jqEv"),
            Pubkey.from_string("APx2hFAqRAtbN6N7LdvYzDCtqGMGWySqVuvg9iMWfkZ8"),
            Pubkey.from_string("H2RDp9L9Tfzp5jzAssNoMCpK2MmLrwJv1wnorEaHS2jJ"),
            Pubkey.from_string("c3kdNx3v9iM4TPUvsZVrgXc5fS9CQz11BBnS62VsB8e"),
            Pubkey.from_string("8cCG6AuMs8aqMN9vLdueYL6Q1kW35EGPBKcRDSyzKMga"),
            Pubkey.from_string("5xSPk47YF3HCoU4wA4HR6KmzQK9whiA8HeUMBcGo9HXn"),
            Pubkey.from_string("BWhHgAgRXoyLfTU33iZ31ME2bk6WTYZxSr74eUqJsJUM"),
            Pubkey.from_string("FT174PMhUBye3qvdy2T1qncDc5pUsc5hTpn7xuXrCPXn"),
            Pubkey.from_string("VdYom29m1yXemVTYFm1cw8Ycu7yzScxyzvG4P63wfW2"),
            Pubkey.from_string("9Lsei9qMonizuuusFgdh94djt7fpgktGmh9PRi2j2GUQ"),
            Pubkey.from_string("EU9uvnDuqNgunfmnxNAjhYi8iEKV3m7gnr5vatg2tgPj"),
            Pubkey.from_string("7dbob1psH1iZBS7qPsm3Kwbf5DzSXK8Jyg31CTgTnxH5"),
            Pubkey.from_string("3F4cdKDeLpvnUtxJ45ue4gs5kCZmhaeLDXN77RHGPfHu"),
            Pubkey.from_string("GkjperyMoy6MCUyg73KzZy4WbfaRhKYAoTBjW3JRjYuG"),
            Pubkey.from_string("8KTa6xFc1dTpm7fsSDKMe5zftHzC6mCR38f7XUp6ugqs"),
            Pubkey.from_string("2iuKYW8qnPPjeWn9rpJUdJQvNWM2CyiSFZNprUFtcYQm"),
            Pubkey.from_string("2FEs2ttf6vauffHDhvWf6F3HANB26iiSULxNF3FAdW1d"),
            Pubkey.from_string("5raajUcFKgaRbyh6yRkAKWroLe6PwtgCAU1vT7wmmpFu"),
            Pubkey.from_string("7Hz86pfpm5hxmzuJbNFbfJ8LEU8EnLL7fc3oyFgVrm5G"),
            Pubkey.from_string("FYpmTRddSQufU9ZrwPHgAj39epj4dP3Qwfdznm3oC5SY"),
            Pubkey.from_string("jQdzjLTZg7fQWGuWHjZmrkTjDNQ3DrAVKkzWvXVrzRm"),
            Pubkey.from_string("DdFzaannSyXs12sB517GbtCsZihh8X9RS2ZKJKuTp5sG"),
            Pubkey.from_string("2Vaf7yEBXi86SGhDM79w1dRQxz5NC2YFWshm5NxkRUDB"),
            Pubkey.from_string("7RxdEbZV3ec7jfbUzVPucaDBY3KRY4FS797rmHHzYQSo"),
            Pubkey.from_string("3Qrw5r74ZgwXLnuTgbYeA8WnHNJDoZEpEZXK3HAuwf21"),
            Pubkey.from_string("Er174YjnV2nuAacfV4nYCAFBgJ6cTgJNaYNp5xPwGZUq"),
            Pubkey.from_string("GWHvCw2WA6s1Vg42ahghWveQTf9t3fc2TnCPFm83L5a4"),
            Pubkey.from_string("ALaSAUhuQtakYNgy5HjqrRQHMfCZ3BV2eUPrenPkPEpZ"),
            Pubkey.from_string("9tbfxk5eVmgMmHGt4JBbp3PnH3Q9QCq1k5puahsqaR8n"),
            Pubkey.from_string("4E2zitVTKfaJB91DJ3JvCR9yr3KcRAKmHee3GQcqmqMu"),
            Pubkey.from_string("APNsyPLc1dNRzwk9C6puX8s7vtUFC6U2o7wyZ7kxk3GV"),
            Pubkey.from_string("CJK3xFSe7WhMDz69vLBhAk3x5PaoXBTc8ep39XUEFhLg"),
            Pubkey.from_string("HWStMu8eEqcKyf7jaLVuKEjVjwRhsZ47uC28QmuMxAzs"),
            Pubkey.from_string("7cwSf9v33vH7HDcbD9fLTa7Dwr6e91f8C3aUMHuNkvHg"),
            Pubkey.from_string("MPT1KEM3kE5XQZCYrMrvQqEVUJwdnkgbAhrrwvYeYa1"),
            Pubkey.from_string("CcRDwd4VYKq5pmUHHnzwujBZwTwfgE95UjjdoZW7qyEs"),
            Pubkey.from_string("8W6mHYDt7Sd6VXWy7Sh82RX68PB2hrFy7KuwkraMbVH2"),
            Pubkey.from_string("2SgUVRAWs1yuUjiYW8JCHb4g7R2gBHdEk5x9KJgn9zNy"),
            Pubkey.from_string("CS4jRF49KnrFfDoSnC6LbRiz7oK5xJCYcSavdp7erJJd"),
            Pubkey.from_string("AY6wqJ3ZjBYXmXKrpa7mZ7NcrqUF4w1KsH2zPGgMszyG"),
            Pubkey.from_string("33ET7TdFt1kVuY2eVjU4rCnCzyKgfiZY9TbPSHb4zCHn"),
            Pubkey.from_string("CdES4frNaF9AvE1Hyso6wbW3jaB1jR7HpZiSNSP4bC7m"),
            Pubkey.from_string("4qdMQ6iLN8Mm4Sa8geNkF1E2PmYN4zB9mGdeW4kxMGBY"),
            Pubkey.from_string("6wmWjNJPNCw3p3psBZM3DURJaxENVk4woYvJsCdcMb7R"),
            Pubkey.from_string("HpTGysQZFppoLQcRrfFu47teEajxharPP7f19XJuKU16"),
            Pubkey.from_string("ygRrmycNpMzEsqLYRpDMS9J1SHaFMG4Rm3tjkyVGVnc"),
            Pubkey.from_string("EV1UdC9dSz7a66hqYW5TkVe6JihSAyfEwVLwYzy1cGXz"),
            Pubkey.from_string("6B23K3tkb51vLZA14jcEQVCA1pfHptzEHFA93V5dYwbT"),
            Pubkey.from_string("EPgAyxa8GJiQzy9pgiTA3bRinxfzyiNxDhorr1KGUznB"),
            Pubkey.from_string("AXrWGEh3c8Jiz2Uhr6kiUxYypjgVYanm48jSWhXjudV8"),
            Pubkey.from_string("8CCrvJUSFta3HMRSFSM5M1LUX2MeFHT5Wcgjo55HQCqC"),
            Pubkey.from_string("7iXjCwhQg9sVys8Ze7Ybusf7WECJBABAmWvGxVMVfX7F"),
            Pubkey.from_string("GcMVDi71RqWuBGgxSo8LKPoSCSkzPXAGmMnr3t5fJZar"),
            Pubkey.from_string("FnDtHqrTuySW94Yy3QFYjMtvyYuJkRp3H6xtDDG1Ehi"),
            Pubkey.from_string("KsUoxhYnaTUFTJ6SuAdAAmUBVrExhCq7SXE7BCu5irh"),
            Pubkey.from_string("9JZFuP5C78QvDrz3HucskAU6uog3XkoEa4Tbwxs3TTgY"),
            Pubkey.from_string("HHvs3T3rcFnZFiTdKn5eXwg1w9ADGB98CpyprHW7jYMB"),
            Pubkey.from_string("GpvkM2TeZXqQzFtBBgqoJYfc3BPScEHaSk41dwMrsKiW"),
            Pubkey.from_string("H3j7orNNo7pzzHJZ1WFsrpJAxWCiE8QW3aatbGufu2PC"),
            Pubkey.from_string("GbgH1oen3Ne1RY4LwDgh8kEeA1KywHvs5x8zsx6uNV5M"),
            Pubkey.from_string("7kK6k11pi8QVvo7zJGbiHR2UCHBYrW9zPQ3fWzWk4RsH"),
            Pubkey.from_string("Bdbf9vq1uFucPdFCvpqEuDYnJgLhdgDG7qyFuNgyX1yn"),
            Pubkey.from_string("5bscSoiVE5n6eXt5vWdYobYaNiifCkFxAPsD9HQ2wCff"),
            Pubkey.from_string("7BctkfW23C3wn3wXBn1SCkZs59sjSUCr6aLeLnDpipY8"),
            Pubkey.from_string("4pu3Wv5xKeuTTeBaWxu2qDFhyQsy2pZVfdarCA5oeor9"),
            Pubkey.from_string("975f8PQYUDjRB2Cb5AMhMvuGdtZ9QTN3BmZ9CwgUeKBc"),
            Pubkey.from_string("8cMRt9XEWvvmAHPk4gGrELwjBcGbVwsZBmsw88DJKBui"),
            Pubkey.from_string("2YwQ84B94mAYsRU5CHzW7Nmok1C9UQbg1bhWdJNKSWE9"),
            Pubkey.from_string("BLcCj2afh19jgkBSC4rXgWsP19cnNs2HUNHpnsVzVsmi"),
            Pubkey.from_string("GdCnmCAMVmWkEBBXhzT6wjtjuWYT6kxatQEuRVdmp7rw"),
            Pubkey.from_string("AofYjza6fUWPMUnrXt2mpFs1Z19Pbqpt6jddMLZtP3c9"),
            Pubkey.from_string("9TSGDwcPQX4JpAvZbu2Wp5b68wSYkQvHCvfeBjYcCyC"),
            Pubkey.from_string("7QVKAbXvB6GqHLQhhM9Aj921asgzWL45QVd6j2hyGjjP"),
            Pubkey.from_string("3Ey7Y7o7gf4GtaWvhsrMwzHoEacEMhmmh9QQUZxdwxfD"),
            Pubkey.from_string("3pMwdhwEDNJaGLnW4XCKfaTfrrZisKtXtfNe7MkAFf27"),
            Pubkey.from_string("6YfkgfPy6GS1V571etgjk6c9bhXxDJmnuWfcCkV8sQS9"),
            Pubkey.from_string("BEbJ8eMVknahSDqGkyREE2Bm7MJkAounDvTfYnpVjTfA"),
            Pubkey.from_string("7rNJEJBevis6xjuGCqdijdgaVroYmkVswnywDxZV8dbP"),
            Pubkey.from_string("BsWCDy6ZdYC4YXLmMmkRV9wCBxirCQpzQgAasQh8SMMy"),
            Pubkey.from_string("8tjshdGp6cPyPV797CXs8r9aTUs3MGsgxr7vvpkQwifv"),
            Pubkey.from_string("DTUy4MRxe1Vj6BcDwZNo5BnvN4Q2UqMKaqHhRqKndpoG"),
            Pubkey.from_string("8rq8Z7hpk1mbaP61KremihYfBLyJ4hCZ4xBhBUCBC8bP"),
            Pubkey.from_string("5oXbnF6JLwEbEc8gt91aTWyjeEAYVG21WdqK2KxeA2MR"),
            Pubkey.from_string("6UxPR2nXJNNM1nESVWGAf8NXMVu3SGgYf3ZfUFoGB9cs"),
            Pubkey.from_string("6o2AifckJtQnwwg8Ee82iFkpocGpJRr3pY9jM7zeNCH1"),
            Pubkey.from_string("CWY7nSGmkLAedL36cdc6cQYCdHGy9sUCV16vTNoupuw1"),
            Pubkey.from_string("9e1DZ5mKwUvFsGyBBuCh9DCJmwx72fpyDBsYo3gsGCwY"),
            Pubkey.from_string("6G5yk3YcJBWPM7SzZbhUsvhZLsEmonqTvc3FqQGdRA81"),
            Pubkey.from_string("2hFnuSe5wWvAu1kxwjNGngtLDXpUWiVpc7UvbNTTkZtg"),
            Pubkey.from_string("9ySay4rVbFDDffUHQrCfkq6WcK4oWdxyfquFcunxxbcR"),
            Pubkey.from_string("GdeTNiTU4sh5a3KAUPMgcVQkU7XQFNQyqQh4EE1KsMAT"),
            Pubkey.from_string("6cAKFTvynML7tR8LLQ1u2UwPorc7TibdvdqjouLquSwD"),
            Pubkey.from_string("CJESiofGZkrKmVYYR2DCtfxAj2h1jdT9oV6EsdfbYZjr"),
            Pubkey.from_string("6ZfjZUd2pgmcevfL6aLTGzpTsLoNyi8pxuboDUnrVf23"),
            Pubkey.from_string("5xt8uuStpThtSX1PqHeiJuWtXZFpnkrrTtHDK1srXuL8"),
            Pubkey.from_string("64x2TaUVMrmxGDCcWYntWR8TPrXA3uaC8TfX9997Kam"),
            Pubkey.from_string("9B4PFGmEdibZh7Fwvg4NPoqZ3KjtQkfz8EnyAr6sxszf"),
            Pubkey.from_string("GJDxkYwrjyupJcp3GQcfiM15nVzYGgxKMsiQzFpz9LUW"),
            Pubkey.from_string("AuzJxhMbxSbUq7RKjAHTGemZ7DoWVmLFfj5vwioJZSF"),
            Pubkey.from_string("GPtuEQszwRvhvy5fQK5ddxnttjC4iqADi3TAi1PRLngB"),
            Pubkey.from_string("2wt9ASn4PU8uRxs2VUzkF3zBCUit7jbyFR96tgXjSrR9"),
            Pubkey.from_string("8oZoCiupH7BcDzoCvJs7KCWLESiFhtPAu5aiGpFvVXiD"),
            Pubkey.from_string("BF5HeyXT9nQANpGyfBdQGoXpYVUvdT4KcWegsRuLUPJz"),
            Pubkey.from_string("8CuMWJhaKrvDPaGSXgYGWBJFT4KQba1ANp2qY9yVL9XL"),
            Pubkey.from_string("jtQC6mgQBSa8JunCFJ7wEaSLEPqoh6nSr4YsyrynAn4"),
            Pubkey.from_string("Ei1V6fVHunDQ7UHredBstwgwKgM1sTt4LXpZtt36kgUE"),
            Pubkey.from_string("H3GDXubBg7VxYeAXoJe1wwomtyBDZa74WHhnUrr2jxUT"),
            Pubkey.from_string("5jdovW9tF9p4Wzd5SECyq8nE2ujgf5ZguqE8HHcHenw3"),
            Pubkey.from_string("W9VbvSDaP31uLZyssKNsJ8vAFnKu1QBWycqca3sKDB1"),
            Pubkey.from_string("A6N3fJFZttRg7pEQHAsYFK19JeyhWqH7pWUjTuNctEnt"),
            Pubkey.from_string("GUDahxAyLdXxXEb7QfraF9JHuAei2y7FXePdqtMRgCcq"),
            Pubkey.from_string("79NZMnUoRLx4BMRPbHfXpqSNdFedVPoocKy5LBo5NyvW"),
            Pubkey.from_string("ENaw1zhxzgPn1yzpb5mGhtSJ6QcxYCwq3RE5NScR6sym"),
            Pubkey.from_string("FaQqp4jQXYcBAwxzbxhozeHmuGu4E2TDz5ZZVoiLprkg"),
            Pubkey.from_string("FGjvPD1eV4h4g9jD3sUDBsyPRtUksaqCQobmn4v5qgGA"),
            Pubkey.from_string("HdnQamWxgfguJVNUvu7c4j3tdP7BjuAXys1PUes7CBru"),
            Pubkey.from_string("ABA56r7csXeZBp6iuEney8jbDLYtAjxB6DGQZ1v1UHHV"),
            Pubkey.from_string("AeULYb1SLHrAXD3vhqfwLt83YgpesBJ75ucDyRUMKVJw"),
            Pubkey.from_string("AeAYpusnB1TUxy8tajh6wZo6PedRm3CYsRdhEtUxUgZe"),
        ],
    ),
}

MAINTAINER_REFERRAL = Pubkey.from_string("DsuAVWxrAv7b5kVJLLDTxMREdG7pasJWgAF2461dmocR")  # xoxo <3

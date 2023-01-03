from artdex_indexer.types.single_artdex_pool.parameter.withdraw_nf_ts import WithdrawNFTsParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_withdraw_nfts(
    ctx: HandlerContext,
    withdraw_nfts: Transaction[WithdrawNFTsParameter, SingleArtdexPoolStorage],
) -> None:
    ...
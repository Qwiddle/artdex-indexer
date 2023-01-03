from artdex_indexer.types.single_artdex_pool.parameter.deposit_nf_ts import DepositNFTsParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_deposit_nfts(
    ctx: HandlerContext,
    deposit_nfts: Transaction[DepositNFTsParameter, SingleArtdexPoolStorage],
) -> None:
    ...
from artdex_indexer.types.single_artdex_pool.parameter.n_ft2_token import NFT2TokenParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_nft_to_token(
    ctx: HandlerContext,
    nft_to_token: Transaction[NFT2TokenParameter, SingleArtdexPoolStorage],
) -> None:
    ...
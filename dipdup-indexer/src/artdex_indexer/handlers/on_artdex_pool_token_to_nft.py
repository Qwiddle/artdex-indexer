from artdex_indexer.types.single_artdex_pool.parameter.token_to_nft import Token2NFTParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_token_to_nft(
    ctx: HandlerContext,
    token_to_nft: Transaction[Token2NFTParameter, SingleArtdexPoolStorage],
) -> None:
    ...
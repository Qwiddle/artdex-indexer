from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Origination


async def on_artdex_origination(
    ctx: HandlerContext,
    single_artdex_pool_origination: Origination[SingleArtdexPoolStorage],
) -> None:
    ...
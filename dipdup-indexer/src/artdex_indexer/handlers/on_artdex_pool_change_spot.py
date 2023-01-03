from artdex_indexer.types.single_artdex_pool.parameter.change_spot import ChangeSpotParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_change_spot(
    ctx: HandlerContext,
    change_spot: Transaction[ChangeSpotParameter, SingleArtdexPoolStorage],
) -> None:
    ...
from artdex_indexer.types.single_artdex_pool.parameter.change_delta import ChangeDeltaParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_change_delta(
    ctx: HandlerContext,
    change_delta: Transaction[ChangeDeltaParameter, SingleArtdexPoolStorage],
) -> None:
    ...
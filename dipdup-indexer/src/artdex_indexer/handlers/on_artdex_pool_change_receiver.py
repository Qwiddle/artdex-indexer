from artdex_indexer.types.single_artdex_pool.parameter.change_receiver import ChangeReceiverParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_change_receiver(
    ctx: HandlerContext,
    change_receiver: Transaction[ChangeReceiverParameter, SingleArtdexPoolStorage],
) -> None:
    ...
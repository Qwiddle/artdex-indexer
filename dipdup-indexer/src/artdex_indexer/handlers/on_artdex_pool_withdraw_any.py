from artdex_indexer.types.single_artdex_pool.parameter.withdraw_any import WithdrawAnyParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_withdraw_any(
    ctx: HandlerContext,
    withdraw_any: Transaction[WithdrawAnyParameter, SingleArtdexPoolStorage],
) -> None:
    ...
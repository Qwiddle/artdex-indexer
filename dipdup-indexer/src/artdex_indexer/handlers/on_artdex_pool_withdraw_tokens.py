from artdex_indexer.types.single_artdex_pool.parameter.withdraw_tokens import WithdrawTokensParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_withdraw_tokens(
    ctx: HandlerContext,
    withdraw_tokens: Transaction[WithdrawTokensParameter, SingleArtdexPoolStorage],
) -> None:
    ...
from artdex_indexer.types.single_artdex_pool.parameter.deposit_tokens import DepositTokensParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_deposit_tokens(
    ctx: HandlerContext,
    deposit_tokens: Transaction[DepositTokensParameter, SingleArtdexPoolStorage],
) -> None:
    ...
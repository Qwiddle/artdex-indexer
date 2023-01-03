import artdex_indexer.models as models

from artdex_indexer.types.single_artdex_pool.parameter.withdraw_tokens import WithdrawTokensParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_withdraw_tokens(
    ctx: HandlerContext,
    withdraw_tokens: Transaction[WithdrawTokensParameter, SingleArtdexPoolStorage],
) -> None:
    contract = withdraw_tokens.data.target_address
    amount = withdraw_tokens.parameter.__root__

    try:
        pool = await models.Pool.get(contract=contract)

        pool.reserve = pool.reserve - int(amount)
        await pool.save()
    
    except Exception as e:
        print("Error in on_artdex_pool_withdraw_tokens " + contract)
        print(e)
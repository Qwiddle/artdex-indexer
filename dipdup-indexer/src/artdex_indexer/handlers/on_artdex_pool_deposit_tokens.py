import artdex_indexer.models as models

from artdex_indexer.types.single_artdex_pool.parameter.deposit_tokens import DepositTokensParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_deposit_tokens(
    ctx: HandlerContext,
    deposit_tokens: Transaction[DepositTokensParameter, SingleArtdexPoolStorage],
) -> None:
    contract = deposit_tokens.data.target_address
    amount = deposit_tokens.parameter.__root__

    try:
        pool = await models.Pool.get(contract=contract)
        
        pool.reserve = pool.reserve + int(amount)
        await pool.save()
    
    except Exception as e:
        print("Error in on_artdex_pool_deposit_nfts " + contract)
        print(e)
import artdex_indexer.models as models

from artdex_indexer.types.single_artdex_pool.parameter.change_fee import ChangeFeeParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_change_fee(
    ctx: HandlerContext,
    change_fee: Transaction[ChangeFeeParameter, SingleArtdexPoolStorage],
) -> None:
    contract = change_fee.data.target_address
    fee = int(change_fee.data.parameter_json)

    try:
        await models.Pool.filter(contract=contract).update(fee=fee)

    except Exception as e:
        print("Error in on_artdex_pool_change_fee " + contract)
        print(e)
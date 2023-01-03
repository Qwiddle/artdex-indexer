import artdex_indexer.models as models

from artdex_indexer.types.single_artdex_pool.parameter.change_spot import ChangeSpotParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_change_spot(
    ctx: HandlerContext,
    change_spot: Transaction[ChangeSpotParameter, SingleArtdexPoolStorage],
) -> None:
    contract = change_spot.data.target_address
    spot_price = int(change_spot.data.parameter_json)

    try:
        await models.Pool.filter(contract=contract).update(spot_price=spot_price)
        
    except Exception as e:
        print("Error in on_artdex_pool_change_spot " + contract)
        print(e)
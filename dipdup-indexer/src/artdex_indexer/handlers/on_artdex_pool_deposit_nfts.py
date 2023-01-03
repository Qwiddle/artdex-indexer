import artdex_indexer.models as models

from artdex_indexer.types.single_artdex_pool.parameter.deposit_nf_ts import DepositNFTsParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_deposit_nfts(
    ctx: HandlerContext,
    deposit_nfts: Transaction[DepositNFTsParameter, SingleArtdexPoolStorage],
) -> None:
    contract = deposit_nfts.data.target_address
    nft_id_list = deposit_nfts.parameter.__root__

    try:
        pool = await models.Pool.get(contract=contract)

        # check if id exists in pool already, 
        # if not, set dict value of key id to 1. or, increase value by 1.
        
        for id in nft_id_list:
            if pool.id_list.get(id) == None:
                pool.id_list[id] = 1
            else:
                pool.id_list[id] = pool.id_list[id] + 1

        await pool.save()

    except Exception as e:
        print("Error in on_artdex_pool_deposit_nfts " + contract)
        print(e)
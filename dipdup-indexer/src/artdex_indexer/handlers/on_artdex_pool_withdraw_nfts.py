import artdex_indexer.models as models

from artdex_indexer.types.single_artdex_pool.parameter.withdraw_nfts import WithdrawNFTsParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_withdraw_nfts(
    ctx: HandlerContext,
    withdraw_nfts: Transaction[WithdrawNFTsParameter, SingleArtdexPoolStorage],
) -> None:
    contract = withdraw_nfts.data.target_address
    nft_id_list = withdraw_nfts.parameter.__root__

    try:
        pool = await models.Pool.get(contract=contract)
        
        # check if value of key id is = 1.
        # if so, delete item from the id_list dict. or, decrease the value by one.

        for id in nft_id_list:
            value = pool.id_list[id]

            if int(value) == 1:
                del pool.id_list[id]
            else:
                pool.id_list[id] = int(value) - 1

        await pool.save()
        
    except Exception as e:
        print("Error in on_artdex_pool_withdraw_nfts " + contract)
        print(e)
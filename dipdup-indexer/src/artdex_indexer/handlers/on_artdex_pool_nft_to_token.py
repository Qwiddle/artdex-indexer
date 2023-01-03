import artdex_indexer.models as models

from artdex_indexer.types.single_artdex_pool.parameter.n_ft2_token import NFT2TokenParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_nft_to_token(
    ctx: HandlerContext,
    nft_to_token: Transaction[NFT2TokenParameter, SingleArtdexPoolStorage],
) -> None:
    contract = nft_to_token.data.target_address
    spot_price = nft_to_token.data.storage['spot_price']
    reserve = nft_to_token.data.storage['reserve']
    nft_id_list = nft_to_token.parameter.nft_ids
    min_tokens_out = nft_to_token.parameter.min_tokens_out
    _to=nft_to_token.parameter._to

    try:
        await models.Swap(
          contract=contract,
          nft_ids=nft_id_list,
          min_tokens_out=min_tokens_out,
          to=_to
        ).save()

        pool = await models.Pool.get(contract=contract)

        # check if id exists in pool already, 
        # if not, set dict value of key id to 1. or, increase value by 1.

        for id in nft_id_list:
            if pool.id_list.get(id) == None:
                pool.id_list[id] = 1
            else:
                pool.id_list[id] = pool.id_list[id] + 1
        
        pool.reserve = reserve
        pool.spot_price = spot_price

        await pool.save()

    except Exception as e:
        print("Error in on_artdex_pool_nft_to_token " + contract)
        print(e)
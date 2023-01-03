import artdex_indexer.models as models

from artdex_indexer.types.single_artdex_pool.parameter.token_to_nft import Token2NFTParameter
from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_artdex_pool_token_to_nft(
    ctx: HandlerContext,
    token_to_nft: Transaction[Token2NFTParameter, SingleArtdexPoolStorage],
) -> None:
    contract = token_to_nft.data.target_address
    spot_price = token_to_nft.data.storage['spot_price']
    reserve = token_to_nft.data.storage['reserve']
    nft_id_list = token_to_nft.parameter.nft_ids
    max_tokens_in = token_to_nft.parameter.max_tokens_in
    _to=token_to_nft.parameter._to

    try:
        await models.Swap(
          contract=contract,
          nft_ids=nft_id_list,
          max_tokens_in=max_tokens_in,
          to=_to
        ).save()

        pool = await models.Pool.get(contract=contract)

        # check if value of key id is = 1.
        # if so, delete item from the id_list dict. or, decrease the value by one.
        
        for id in nft_id_list:
            value = pool.id_list[id]

            if value == 1:
                del pool.id_list[id]
            else:
                pool.id_list[id] = value - 1

        pool.reserve = reserve
        pool.spot_price = spot_price

        await pool.save()

    except Exception as e:
        print("Error in on_artdex_pool_token_to_nft " + contract)
        print(e)
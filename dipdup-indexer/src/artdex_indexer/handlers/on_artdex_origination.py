import artdex_indexer.models as models

from artdex_indexer.types.single_artdex_pool.storage import SingleArtdexPoolStorage
from dipdup.context import HandlerContext
from dipdup.models import Origination


async def on_artdex_origination(
    ctx: HandlerContext,
    single_artdex_pool_origination: Origination[SingleArtdexPoolStorage],
) -> None:
    try:
        id_list = single_artdex_pool_origination.data.storage['id_list']
        new_id_list = {}

        # convert values from id_list to integers
        for key, value in id_list.items():
            new_id_list[key] = int(value)

        originated_contract = single_artdex_pool_origination.data.originated_contract_address
        index_name = f'artdex_factory_{originated_contract}'

        if index_name not in ctx.config.indexes:
            await ctx.add_contract(
                name=originated_contract,
                address=originated_contract,
                typename='single_artdex_pool',
            )
            
            await ctx.add_index(
                name=index_name,
                template='artdex_pool',
                values={'contract': originated_contract, 'datasource': 'tzkt'},
            )

            await models.Pool(
              contract=originated_contract,
              id_list=new_id_list,
              payment_token_fa2=single_artdex_pool_origination.data.storage['payment_token']['fa2_address'],
              payment_token_id=single_artdex_pool_origination.data.storage['payment_token']['token_id'],
              fee=single_artdex_pool_origination.data.storage['fee'],
              delta=single_artdex_pool_origination.data.storage['delta'],
              spot_price=single_artdex_pool_origination.data.storage['spot_price'],
              reserve=single_artdex_pool_origination.data.storage['reserve'],
              collection_address=single_artdex_pool_origination.data.storage['nft_collection_address'],
            ).save()
    except Exception as e:
        print("Error in on_artdex_origination: " + single_artdex_pool_origination.data.originated_contract_address)
        print(e)
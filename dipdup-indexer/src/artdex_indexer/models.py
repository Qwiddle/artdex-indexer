from tortoise import fields
from dipdup.models import Model


class Pool(Model):
    contract = fields.CharField(36, pk=True)
    id_list = fields.JSONField()
    fee = fields.BigIntField()
    delta = fields.BigIntField()
    payment_token_fa2 = fields.CharField(36)
    payment_token_id = fields.IntField()
    reserve = fields.BigIntField()
    spot_price = fields.BigIntField()
    collection_address = fields.CharField(36, index=True)
  
class Swap(Model):
    contract = fields.CharField(36, index=True)
    nft_ids = fields.CharField(255)
    max_tokens_in = fields.BigIntField(null=True)
    min_tokens_out = fields.BigIntField(null=True)
    to = fields.CharField(36, index=True)
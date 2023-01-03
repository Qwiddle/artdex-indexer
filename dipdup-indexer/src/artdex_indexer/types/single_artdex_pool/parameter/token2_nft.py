# generated by datamodel-codegen:
#   filename:  token2NFT.json

from __future__ import annotations

from typing import List

from pydantic import BaseModel
from pydantic import Extra


class Token2NFTParameter(BaseModel):
    class Config:
        extra = Extra.allow

    _to: str
    max_tokens_in: str
    nft_ids: List[str]
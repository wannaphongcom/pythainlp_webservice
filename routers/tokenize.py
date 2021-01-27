from fastapi import APIRouter
from pythainlp import tokenize
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()


class TokenizeEngine(str, Enum):
    newmm = "newmm"
    longest = "longest"
    deepcut = "deepcut"
    icu = "icu"
    ulmfit = "ulmfit"


class WordTokenizeResponse(BaseModel):
    words: List[str] = []


@router.get('/word_tokenize', response_model=WordTokenizeResponse)
def word_tokenize(q: str, engine: TokenizeEngine = "newmm"):
    return {"words": tokenize.word_tokenize(q, engine=engine)}

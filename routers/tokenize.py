from fastapi import APIRouter
from pythainlp import tokenize
from enum import Enum

router = APIRouter()

class TokenizeEngine(str, Enum):
    newmm = "newmm"
    longest = "longest"
    deepcut = "deepcut"
    icu = "icu"
    ulmfit = "ulmfit"

@router.get('/word_tokenize')
def word_tokenize(q: str, engine: TokenizeEngine = "newmm"):
    return '|'.join(tokenize.word_tokenize(q,engine=engine))

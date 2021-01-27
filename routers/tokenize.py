from fastapi import APIRouter
from pythainlp import tokenize
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()


class SentTokenizeEngine(str, Enum):
    whitespace = "whitespace"
    whitespace_newline = "whitespace+newline"


class WordTokenizeEngine(str, Enum):
    newmm = "newmm"
    longest = "longest"
    deepcut = "deepcut"
    icu = "icu"
    ulmfit = "ulmfit"


class SubwordTokenizeEngine(str, Enum):
    tcc = "tcc"
    etcc = "etcc"


class SentTokenizeResponse(BaseModel):
    sents: List[str] = []


class WordTokenizeResponse(BaseModel):
    words: List[str] = []


class SyllableTokenizeResponse(BaseModel):
    syllables: List[str] = []


class SubwordTokenizeResponse(BaseModel):
    subwords: List[str] = []


@router.get('/sent', response_model=SentTokenizeResponse)
def sent_tokenize(q: str, engine: SentTokenizeEngine = "whitespace"):
    return {"sents": tokenize.sent_tokenize(q, engine=engine)}


@router.get('/word', response_model=WordTokenizeResponse)
def word_tokenize(q: str, engine: WordTokenizeEngine = "newmm"):
    return {"words": tokenize.word_tokenize(q, engine=engine)}


@router.get('/syllable', response_model=SyllableTokenizeResponse)
def syllable_tokenize(q: str):
    return {"syllables": tokenize.syllable_tokenize(q)}


@router.get('/subword', response_model=SubwordTokenizeResponse)
def subword_tokenize(q: str, engine: SubwordTokenizeEngine = "tcc"):
    return {"subwords": tokenize.subword_tokenize(q, engine=engine)}

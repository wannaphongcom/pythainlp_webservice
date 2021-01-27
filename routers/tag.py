from fastapi import APIRouter, Query
from enum import Enum
from typing import List, Optional, Tuple
from pydantic import BaseModel
from pythainlp import tag, tokenize
from pythainlp.tag.named_entity import ThaiNameTagger

router = APIRouter()
ner = ThaiNameTagger()


class PosTagEngine(str, Enum):
    perceptron = "perceptron"
    unigram = "unigram"
    artagger = "artagger"


class CorpusEngine(str, Enum):
    orchid = "orchid"
    orchid_ud = "orchid_ud"
    pud = "pud"


class PosTag(BaseModel):
    word: str
    pos: str


class NERTag(BaseModel):
    word: str
    pos: str
    ner: str


class PosTagResponse(BaseModel):
    pos_tags: List[PosTag] = []


class NERResponse(BaseModel):
    ner_tags: List[NERTag] = []


@router.get('/pos', response_model=PosTagResponse)
def pos_tag(q: str = "", words: List[str] = Query(None), engine: PosTagEngine = "perceptron", corpus: CorpusEngine = "orchid"):
    if len(q) != 0:
        words = tokenize.word_tokenize(q)
    tags = tag.pos_tag(words, engine=engine, corpus=corpus)
    res = [{"word": word, "pos": pos} for word, pos in tags]
    return {"pos_tags": res}


@router.get('/provinces', response_model=PosTagResponse)
def tag_provinces(q: str = "", words: List[str] = Query(None)):
    if len(q) != 0:
        words = tokenize.word_tokenize(q)
    tags = tag.tag_provinces(words)
    res = [{"word": word, "pos": pos} for word, pos in tags]
    return {"pos_tags": res}


@router.get('/ner', response_model=NERResponse)
def get_ner(q: str = ""):
    tags = ner.get_ner(q)
    res = [{"word": word, "pos": pos, "ner": ner} for word, pos, ner in tags]
    return {"ner_tags": res}

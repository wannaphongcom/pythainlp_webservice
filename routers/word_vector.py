from fastapi import APIRouter, Query, HTTPException
from pythainlp import word_vector
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()


class MostSimilarCosmulWord(BaseModel):
    word: str
    score: float


class DoesntMatchResponse(BaseModel):
    doesnt_match: str = ""


class MostSimilarCosmulResponse(BaseModel):
    most_similar_cosmul: List[MostSimilarCosmulWord] = []


class SentenceVectorizerResponse(BaseModel):
    sentence_vectorizer: List[List[float]] = []


class SimilarityResponse(BaseModel):
    similarity: float = -1


@router.get('/doesnt-match', response_model=DoesntMatchResponse)
def doesnt_match(words: List[str] = Query(None)):
    try:
        return {"doesnt_match": word_vector.doesnt_match(words)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e).replace("\"", ""))


@router.get('/most-similar-cosmul', response_model=MostSimilarCosmulResponse)
def most_similar_cosmul(listPositive: List[str] = Query([]), listNegative: List[str] = Query([])):
    try:
        words = word_vector.most_similar_cosmul(listPositive, listNegative)
        res = [{"word": word, "score": score} for word, score in words]
        return {"most_similar_cosmul": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e).replace("\"", ""))


@router.get('/sentence-vectorizer', response_model=SentenceVectorizerResponse)
def sentence_vectorizer(q: str = ""):
    try:
        vector = word_vector.sentence_vectorizer(q, use_mean=True).tolist()
        return {"sentence_vectorizer": vector}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e).replace("\"", ""))


@router.get('/similarity', response_model=SimilarityResponse)
def similarity(word1: str = "", word2: str = ""):
    try:
        return {"similarity": word_vector.similarity(word1, word2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e).replace("\"", ""))

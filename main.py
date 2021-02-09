# -*- coding: utf-8 -*-
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers import tag, tokenize, word_vector
import uvicorn
import pythainlp

DESC_TEXT = "Pythainlp API"

app = FastAPI(
    title='Pythainlp API',
    description=DESC_TEXT,
    version='0.1',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"Pythainlp Version": pythainlp.__version__}


app.include_router(tag.router, prefix="/tag", tags=["Tag"])
app.include_router(tokenize.router, prefix="/tokenize", tags=["Tokenize"])
app.include_router(word_vector.router,
                   prefix="/word-vector", tags=["Word Vector"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

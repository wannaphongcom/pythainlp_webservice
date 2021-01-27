# -*- coding: utf-8 -*-
from fastapi import Depends, FastAPI, Header, HTTPException
from routers import tag, tokenize

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
def hello():
    return {"Hello": "World"}


app.include_router(tag.router)
app.include_router(tokenize.router)

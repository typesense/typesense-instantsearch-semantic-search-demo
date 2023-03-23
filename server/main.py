import json
from sentence_transformers import SentenceTransformer
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

model = SentenceTransformer('all-MiniLM-L6-v2')

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    return {"status": "ok"}


@app.get("/embedding")
def read_embedding(q: Union[str, None] = None):
    sentences = [q]
    sentence_embeddings = model.encode(sentences)

    return {"q": q, "embedding": sentence_embeddings[0].tolist()}

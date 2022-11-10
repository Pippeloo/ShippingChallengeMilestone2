from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def read_root():
    return {"user": "Jules"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
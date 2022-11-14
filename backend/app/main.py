from typing import Union
from fastapi import FastAPI
from .classes.Database import Database

db = Database(
    host="scm2_db_jt",
    database="data",
    user="user",
    password="mysecretpassword",
    port=5432,
)

app = FastAPI()

@app.get("/api/status")
def read_status():
    return db.get_status()


@app.get("/api/user")
def read_user():
    return db.get_user()
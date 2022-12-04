from typing import Union
from fastapi import FastAPI
from .classes.Database import Database
import os

db = Database(
    host="scm2-db-jt",
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

@app.get("/api/hostname")
def read_hostname():
    return {"hostname": os.uname()[1]}
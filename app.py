import os

from fastapi import FastAPI, HTTPException

app = FastAPI()

PASSWORD = os.getenv("CI_CD_PASSWORD")


@app.get("/")
async def welcome():
   
    return {"message": "hello world" }


@app.get("/login")
async def login(password: str):
    if password != PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"message": "Login successful"}
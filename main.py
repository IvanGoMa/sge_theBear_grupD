from typing import List
from fastapi import FastAPI
from services import read

#connecció fastapi
app = FastAPI()

@app.get("/user/read/", response_model=list[dict])
async def read_root():
    results = read.registre()
    return results




#!/usr/bin/python3


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"test": "alta3 research"}


@app.get("/items/{myid}")
async def read_item(myid):
    return {"myid_value": myid}

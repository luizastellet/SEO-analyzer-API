from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from get_data import get_info

app = FastAPI()
origins = ["*"]
url = {"value": ""}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/url")
async def create_URL(data : Request):
    req_info = await data.json()
    url["value"] = req_info["url"]
    return { "url": req_info }

@app.get("/url")
def get_URL():
    return url

@app.get("/page/")
def get_page_info():
    url = get_URL().get("value")
    data = get_info(url)
    return data
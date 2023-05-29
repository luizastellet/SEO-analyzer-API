from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from get_data import get_info

app = FastAPI()
origins = ["*"]
url = {"value": ""}
page = {"data": ""}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/url")
async def save_URL(data: Request):
    req_info = await data.json()
    url["value"] = req_info["url"]
    page["data"] = get_info(url["value"])
    return { "message": "url enviada com sucesso" }

@app.get("/url")
def get_URL():
    return url

@app.get("/page/")
def get_page_info():
    return page["data"]
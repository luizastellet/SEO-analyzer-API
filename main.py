import requests
from bs4 import BeautifulSoup
from header_tags_handler import extract_data, check_keywords, check_title
from utils import check_element_existence 
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]
url = {"value": "https://uenf.br/portal/"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/url")
async def get_URL(data : Request):
    req_info = await data.json()
    url["value"] = req_info["url"]
    print(url)
    return { "url": req_info }

print(url)
# url = 'https://uenf.br/portal/'
res = requests.get(url["value"])
page = res.text

html_page = BeautifulSoup(page, 'html.parser')
html_page.prettify()

head = html_page.head
body = html_page.body
meta = head.find_all('meta')
meta_data = extract_data(meta) 


meta_data = check_element_existence(["description", "keywords"], meta_data)


@app.get("/title")
def get_title():
    title = check_title(html_page.title)
    return {"title": title }

@app.get("/keywords")
def get_keywords():
    keywords = check_keywords(meta_data["keywords"])
    return {"keywords": keywords }

@app.get("/meta")
def get_meta():
    return {"meta_data": meta_data }




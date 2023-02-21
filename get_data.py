import requests
from bs4 import BeautifulSoup
from header_tags_handler import extract_data, check_keywords, check_title
from utils import check_element_existence 

def get_html(url):
    res = requests.get(url)
    page = res.text
    html_page = BeautifulSoup(page, 'html.parser')
    return html_page

def get_meta_data(head):
    meta = head.find_all('meta')
    meta_data = extract_data(meta)
    meta_data = check_element_existence(["description", "keywords"], meta_data)
    return meta_data


def get_info(url):
    html_page = get_html(url)
    head = html_page.head
    body = html_page.body
    meta_data = get_meta_data(html_page)
    title = check_title(html_page.title)
    keywords = check_keywords(meta_data["keywords"])
    
    return {
        "title": title, 
        "keywords": keywords, 
        "meta_data": meta_data
    }


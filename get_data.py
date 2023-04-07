import requests
from bs4 import BeautifulSoup
from header_tags_handler import extract_data, check_keywords, check_title
from utils import check_element_existence
from title_handler import get_title
from images_handler import get_images
from headings_handler import get_headings
from description_handler import get_description
from keyword_handler import count_keywords

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
    result = []
    html_page = get_html(url)
    head = html_page.head
    body = html_page.body
    meta_data = get_meta_data(html_page)
    title = get_title(html_page.title)
    description = get_description(meta_data["description"])
    keywords = count_keywords(meta_data["keywords"], body)
    images = get_images(html_page)
    headings = get_headings(html_page)

    

    return {
        'title': title,
        'headings': headings,
        'images': images,
        'description': description, 
        'keywords': keywords
    }

 
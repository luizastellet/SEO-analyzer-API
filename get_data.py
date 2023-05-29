import requests
from bs4 import BeautifulSoup
from header_tags_handler import extract_data
from utils import check_element_existence
from title_handler import title_analyzer
from images_handler import analyze_images
from headings_handler import headings_analyzer
from description_handler import description_analyzer
from keyword_handler import keywords_density, keyword_location_analyzer
from semantic_tags_handler import get_semantic_tags
from internal_links_handler import get_internal_links
from url_handler import url_analyzer

def get_html(url):
    res = requests.get(url)
    page = res.text

    print(res)
    f = open("html.txt", "w")
    f.write(page)

    html_page = BeautifulSoup(page, 'html.parser')
    return html_page

def get_meta_data(head):
    meta = head.find_all('meta')
    meta_data = extract_data(meta)
    meta_data = check_element_existence(["description", "keywords"], meta_data)
    return meta_data


def get_info(url):
    html_page = get_html(url)
    meta_data = get_meta_data(html_page)
    keywords = meta_data["keywords"].lower()
    description = meta_data["description"]
    title = html_page.title
    title_result = title_analyzer(title)
    description_result = description_analyzer(description)
    internal_links = get_internal_links(url, html_page)
    images = analyze_images(html_page)
    headings = headings_analyzer(html_page)
    keyword_density = keywords_density(keywords, html_page.body)
    keyword_in_url = url_analyzer(url, meta_data["keywords"])
    keyword_location = keyword_location_analyzer(keywords, title, description, html_page)

    return {
        'title': title_result,
        'headings': headings,
        'images': images,
        'description': description_result, 
        'keywords': keyword_density,
    }

 
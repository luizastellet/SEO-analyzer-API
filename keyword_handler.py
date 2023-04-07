from bs4 import BeautifulSoup
import re 
from collections import Counter
from string import punctuation

def count_keywords(keywords_arr, html):
    if keywords_arr is None:
        return [{
            'content': None,
            'type': 'error',
            'errorName': 'A página não possui palavras-chave definidas. ',
            'tag': '<meta name="keywords">',
        }]

    keywords = keywords_arr.split(", ")
    html_str = str(html)
    text_p = (''.join(s.findAll(text=True))for s in html.findAll('p'))
    c_p = Counter((x.rstrip(punctuation).lower() for y in text_p for x in y.split()))
    text_div = (''.join(s.findAll(text=True))for s in html.findAll('div'))
    c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))
    total = c_div + c_p
    

    total_count = 0
    for count in total.values():
        total_count += count
        
    res = []
    for keyword in keywords: 
        matches = re.findall(keyword, html_str, re.IGNORECASE)
        density = (len(matches) / total_count) * 100
        res.append({
            'keyword': keyword, 
            'count': len(matches),
            'density': "%.2f" % density
        })

    return res
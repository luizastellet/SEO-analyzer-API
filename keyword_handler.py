from bs4 import BeautifulSoup
import re 
from collections import Counter
from string import punctuation

def keywords_density(keywords_arr, html):
    if keywords_arr is None:
        return [{
            'content': None,
            'type': 'error',
            'infoText': 'A página não possui palavras-chave definidas. ',
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
        
    result = []
    for keyword in keywords: 
        matches = re.findall(keyword, html_str, re.IGNORECASE)
        density = (len(matches) / total_count) * 100
        result.append({
            'keyword': keyword, 
            'count': len(matches),
            'density': "%.2f" % density
        })

    return result

# ---------------------------------------------------
    heading_list = ['h2', 'h3', 'h4', 'h5', 'h6']
    result = []
    for idx, element in enumerate(heading_list):
        heading_arr = html.find_all(element)
        if (not heading_arr):
                result.append({
                    'content': None,
                    'type': 'warning',
                    'infoText': f'A página não possui o elemento de cabeçalho h{str(idx+2)} .',
                    'tag': f'<h{str(idx+2)}>', 
                })


def keyword_location_analyzer(keywords, title, description, html):
    if keywords is None:
        return [{
            'content': None,
            'type': 'error',
            'infoText': 'A página não possui palavras-chave definidas. ',
            'tag': '<meta name="keywords">',
        }]
    keywords = keywords.split(", ")

    heading_result = []
    title_result = []
    description_result = []
    for keyword in keywords:
        if keyword in title: 
            heading_result.append({
                f'A palavra-chave {keyword} está presente na tag de título. '
            })
        
        if keyword in description: 
            description_result.append({
                f'A palavra-chave {keyword} está presente na meta tag de descrição. '
            })

        for i in range(1, 6):
            heading_arr = html.find_all(f'h{i}') 
            for heading in heading_arr:
                if (heading is not None): 
                    if keyword in heading: 
                        heading_result.append({
                            f'A palavra-chave {keyword} está presente em uma tag h{i}. '
                        })
        
    
    if (not heading_result): 
        heading_result = [{
            'content': None,
            'type': 'error',
            'infoText': 'A página não possui palavras-chaves sem seus elementos de títulos e subtítulos. ',
            'tag': '<h1> ... <h6>',
        }]

    if (not title_result): 
        title_result = [{
            'content': None,
            'type': 'error',
            'infoText': 'Não existem palavras-chaves no título da página.',
            'tag': '<title>',
        }]

    if (not description_result): 
        description_result = [{
            'content': None,
            'type': 'error',
            'infoText': 'Não existem palavras-chaves na descrição da página.',
            'tag': '<title>',
        }]

    return {
        "heading_result": heading_result, 
        "title_result": title_result, 
        "description_result": description_result
    }
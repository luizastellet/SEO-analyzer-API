
def get_others_headings(html):
    heading_list = ['h2', 'h3', 'h4', 'h5', 'h6']
    result = []
    for idx, element in enumerate(heading_list):
        heading_arr = html.find_all(element)
        if (not heading_arr):
                result.append({
                    'content': None,
                    'type': 'error',
                    'infoText': f'A página não possui o elemento de cabeçalho h{str(idx+2)} .',
                    'tag': f'<h{str(idx+2)}>', 
                })
        else:
            for item in heading_arr:
                result.append({
                    'content': str(item.contents),
                    'type': 'info',
                    'infoText': None,
                    'tag': f'<h{str(idx+2)}>',
                }) 

    return result

def analyze_images(html_page):

    images_arr = html_page.find_all('img')
    res = []
    if (not images_arr):
        return [{
            'content': None,
            'type': 'info',
            'infoText': 'A página não possui nenhuma imagem.',
            'tag': '<img>',
        }]

    for item in images_arr:
        if (item["alt"]):
            res.append({
                "url": item["src"],
                'content': item["alt"],
                'type': 'check',
                'infoText': None,
                'tag': '<img>',
            })
        else: 
            res.append({
                "url": item["src"],
                'content': None,
                'type': 'error',
                'infoText': 'Elemento de imagem não possui atributo de texto alternativo.',
                'tag': '<img>',
            })
        

    return res

def h1_analyzer(html):
    h1_arr = html.find_all('h1')

    if (not h1_arr):
        return {
            'content': None,
            'type': 'error',
            'infoText': 'A página não possui o elemento de cabeçalho h1.',
            'tag': '<h1>',
        }

    result = []
    for item in h1_arr:
        result.append(item.string)
    if (len(result) > 1):
        return {
            'content': result,
            'type': 'warning',
            'infoText': 'Uma página não deve possuir mais de um elemento h1.',
            'tag': '<h1>',
        }

    return {
            'content': result,
            'type': 'check',
            'infoText': None,
            'tag': '<h1>',
            }

def others_headings_analyzer(html):
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
        else:
            for item in heading_arr:
                result.append({
                    'content': str(item.contents),
                    'type': 'check',
                    'errorName': None,
                    'tag': f'<h{str(idx+2)}>',
                }) 

    return result

def headings_analyzer(html_page):
    h1 = h1_analyzer(html_page)
    other_headings = others_headings_analyzer(html_page)
    return {
        'h1': h1, 
        'headings' : tuple(other_headings)
    }

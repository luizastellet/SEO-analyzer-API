def get_h1(html):
    h1_arr = html.find_all('h1')

    if (not h1_arr):
        return {
            'content': None,
            'type': 'error',
            'errorName': 'A página não possui o elemento de cabeçalho h1.',
            'tag': '<h1>',
        }

    res = []
    for item in h1_arr:
        res.append(item.string)
    if (len(res) > 1):
        return {
            'content': res,
            'type': 'error',
            'errorName': 'Uma página não deve possuir mais de um elemento h1.',
            'tag': '<h1>',
        }

    return {
            'content': res,
            'type': 'info',
            'errorName': None,
            'tag': '<h1>',
            }

def get_others_headings(html):
    heading_list = ['h2', 'h3', 'h4', 'h5', 'h6']
    result = []
    for idx, element in enumerate(heading_list):
        heading_arr = html.find_all(element)
        if (not heading_arr):
                result.append({
                    'content': None,
                    'type': 'error',
                    'errorName': f'A página não possui o elemento de cabeçalho h{str(idx+2)} .',
                    'tag': f'<h{str(idx+2)}>', 
                })
        else:
            for item in heading_arr:
                result.append({
                    'content': str(item.contents),
                    'type': 'info',
                    'errorName': None,
                    'tag': f'<h{str(idx+2)}>',
                }) 

    return result

def get_headings(html_page):
    h1 = get_h1(html_page)
    headings = get_others_headings(html_page)
    return {
        'h1': h1, 
        'headings' : tuple(headings)
    }



def url_analyzer(url, keywords_arr): 
    if (keywords_arr is None):
        return {
            'content': None,
            'type': 'error',
            'infoText': 'A página não possui palavras-chaves para serem analisadas.',
            'tag': None,
        }
    
    keywords = keywords_arr.split(", ")
    result = []
    for keyword in keywords: 
        if (keyword in url):
            result.append({
                'content': keyword,
                'type': 'check',
                'infoText': f"A palavra-chave {keyword} foi encontrada na URL.",
                'tag': None,
            })

    if (result is None): 
         return {
            'content': None,
            'type': 'error',
            'infoText': 'A página não possui nenhuma palavra-chave em sua URL.',
            'tag': None,
        }

    return result
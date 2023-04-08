def get_title(title):
    if title is None or title.string is None: 
        return [{
            'title': None, 
            'type': 'error',
            'errorName': 'Tag de título não possui conteúdo.',
            'tag': str(title),
        }]
    else: 
        length = len(title.string)
        if length > 50 and length < 60:
            return [{
                'title': title.string,
                'type': 'info',
                'errorName': 'O título possui um tamanho apropriado para aparecer nos resultados de busca, que é entre 50 e 60 caracteres. ',
                'tag': str(title),
            }]
        else: 
            return [{ 
                'title': title.string,
                'type': 'warning',
                'errorName': f'O título da página possui {length} caracteres. O tamanho ideal é entre 50 e 60 caracteres.',
                'tag': str(title),
            }]

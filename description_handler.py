def get_description(description): 
    if description is None:
        return {
            'content': None,
            'type': 'warning',
            'errorName': 'Página não possui meta tag de descrição.',
            'tag': '<meta name=description>',
        }
    
    if (len(description) > 160):
        return {
            'content': description,
            'type': 'warning',
            'errorName': 'A descrição não deve ultrapassar o tamanho de 160 caracteres. ',
            'tag': '<meta name=description>',
        }
    
    return {
        'content': description,
        'type': 'info',
        'errorName': None,
        'tag': '<meta name=description>',
    }
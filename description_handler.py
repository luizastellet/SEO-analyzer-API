def description_analyzer(description): 
    if description is None:
        return {
            'content': None,
            'type': 'error',
            'infoText': 'Página não possui meta tag de descrição ou seu conteúdo está vazio.',
            'tag': '<meta name=description>',
        }
    
    if (len(description) > 160):
        return {
            'content': description,
            'type': 'warning',
            'infoText': 'A descrição não deve ultrapassar o tamanho de 160 caracteres.',
            'tag': '<meta name=description>',
        }
    
    return {
        'content': description,
        'type': 'check',
        'infoText': None,
        'tag': '<meta name=description>',
    }
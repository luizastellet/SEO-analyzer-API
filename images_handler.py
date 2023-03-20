error = [
    { "image_no_alt_text": { 
        'errorType': 'error',
        'errorText': 'Imagem não possui alt text.',
        'errorMessage': 'Textos alternativos são importantes para SEO, pois fornecem contexto ao mecanismo de busca.',
        'errorTag':'image'
        }
    }
]

def get_images(images):
    result = []
    
    # for image in images:
    #     if (image.attrs.get("alt") == ''):
    #         # print(f'{image} \n\n')

    # return img_arr
    # return 'alo'

    # return [{
    #         'title': None, 
    #         'type': 'error',
    #         'errorName': 'Tag de título não possui conteúdo.',
    #         'tag': str(title),
    #     }]
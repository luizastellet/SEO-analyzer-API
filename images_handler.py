error = [
    { "image_no_alt_text": { 
        'errorType': 'error',
        'errorText': 'Imagem não possui alt text.',
        'errorMessage': 'Textos alternativos são importantes para SEO, pois fornecem contexto ao mecanismo de busca.',
        'errorTag':'image'
        }
    }
]

def check_alt_attr(imgs_arr):
    for img in imgs_arr:
        alt = img.attrs.get("alt")
        print(alt)

def func(images):
    check_alt_attr(images)
    # return img_arr
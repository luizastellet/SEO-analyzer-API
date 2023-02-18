from fastapi import FastAPI
app = FastAPI()

def format_error_position(title):
    return "Posição: linha {}, coluna {}. ".format(title.sourceline, title.sourcepos)

def extract_data(data):
    data_dict = {}
    for item in data:
        property_name = item.attrs.get("name")
        property_value = item.attrs.get("content")
        if property_name is not None:
            data_dict.update({property_name: property_value})
    return data_dict


def check_keywords(keywords):
    if keywords is None:
        # error_position = format_error_position(keywords)
        return {
            'errorType': 'error',
            'errorName': 'Tag de keywords deve possuir conteúdo.',
            'errorMessage': 'BLABLABALBALBALAB',
            'errorTag': keywords,
            # 'errorPosition': error_position
        }

    return keywords
    

def check_title(title):
    if title is None:
        error_position = format_error_position(title)
        return {
            'errorType': 'error',
            'errorName': 'Tag de Título deve possuir conteúdo.',
            'errorMessage': 'BLABLABALBALBALAB',
            'errorTag': title,
            'errorPosition': error_position
        }
        
    return title.string
from fastapi import FastAPI
from utils import format_error_position
app = FastAPI()


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
           
        }

    return keywords
    

def check_title(title):
    if title.string is None: 
        return {
            'tagName': 'Title',
            'errorType': 'error',
            'errorName': 'Tag de Título deve possuir conteúdo.',
            'errorMessage': 'BLABLABALBALBALAB',
            'errorTag': str(title),
            'errorPosition': format_error_position(title)
        }
    return 
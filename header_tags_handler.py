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


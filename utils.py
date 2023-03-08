def foreach(iterable, function):
    for element in iterable:
        function(element)


def check_element_existence(elements_arr, data):
    res = {}
    for element in elements_arr:
        if (element in data):
            res.update({ element: data[element]})
        else: 
            res.update({ element: None})
    return res

def format_error_position(element):
    return "Posição: linha {}, coluna {}. ".format(element.sourceline, element.sourcepos)

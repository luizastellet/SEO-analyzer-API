from urllib.parse import urlparse

def get_internal_links(url, html):
    links = html.find_all('a')
    parsed_url = urlparse(url).netloc
    count = 0

    for link in links:
        link_url = (link.attrs.get('href'))
        if link_url is not None and parsed_url in link_url:
            count += 1

    if count == 0:
        return "Esta página não possui nenhum link interno. "
    
    return f"Esta página possui {count} links internos. "
from urllib.parse import urlparse

def get_internal_links(url, html):
    links = html.find_all('a')
    parsed_url = f"{urlparse(url).scheme}://{urlparse(url).netloc}"
    urls = []

    for link in links:
        link_url = (link.attrs.get('href'))
        if parsed_url in link_url:
            urls.append(link_url)


    if len(urls) == 0:
        return "Esta página não possui nenhum link interno. "
    
    return {
        "infoText": f"Esta página possui {len(urls)} links internos. ",
        "links": urls,
    }
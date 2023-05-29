
def get_semantic_tags(html):
    semantic_tags = [
    {
       'tag': 'header',
       'description': 'blablaba'
    },
    {
       'tag': 'section',
       'description': 'blablaba' 
    }, 
    {
       'tag': 'article',
       'description': 'blablaba' 
    }, 
    {
       'tag': 'nav',
       'description': 'blablaba' 
    }, 
    {
       'tag': 'aside',
       'description': 'blablaba' 
    }, 
    {
       'tag': 'main',
       'description': 'blablaba' 
    }, 
    {
       'tag': 'figure',
       'description': 'blablaba' 
    }, 
    {
       'tag': 'footer',
       'description': 'blablaba' 
    }, 
    {
       'tag': 'em',
       'description': 'blablaba' 
    }, 
    {
       'tag': 'strong',
       'description': 'blablaba' 
    }, 
    {
       'tag': 'q',
       'description': 'blablaba'
    },
]
    res = []

    for tag in semantic_tags: 
        tag["hasTag"] = len(html.find_all(tag["tag"])) > 0

    return semantic_tags
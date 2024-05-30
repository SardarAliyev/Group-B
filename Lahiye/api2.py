import requests

def get_wikipedia_page_id(page_title):
    # Vikipediya API URL
    url = "https://en.wikipedia.org/w/api.php"

    # Sorğu parametrləri
    params = {
        "action": "query",
        "format": "json",
        "titles": page_title,
        "redirects": 1
    }

    # Sorğu göndəririk
    response = requests.get(url, params=params)
    data = response.json()

    # Səhifənin ID-sini əldə edirik
    page_id = None
    if 'query' in data and 'pages' in data['query']:
        pages = data['query']['pages']
        page_id = next(iter(pages))  # İlk səhifənin ID-sini götürürük

    return page_id

def test_get_wikipedia_page_id():
    page_title = "Python (programming language)"
    page_id = get_wikipedia_page_id(page_title)
    assert page_id is not None, f"Page ID should not be None for the page title '{page_title}'"
    assert isinstance(page_id, str) or isinstance(page_id, int), f"Page ID should be a string or integer, but got {type(page_id)}"
    print(f"Page ID for '{page_title}': {page_id}")

# Test edirik
test_get_wikipedia_page_id()

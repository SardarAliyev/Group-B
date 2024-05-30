import requests

def test_page_url():
    page_url = "https://en.wikipedia.org/w/api.php?action=query&titles=NASA&prop=info&inprop=url&format=json"
    response = requests.get(page_url)
    if response.status_code == 200:
        data = response.json()
        page_id = list(data['query']['pages'].keys())[0]
        page_info = data['query']['pages'][page_id]
        page_url = page_info['fullurl']
        print("Page URL Endpoint:")
        print("Page URL:", page_url)
        print("Status: Success\n")
    else:
        print("Page URL Endpoint:")
        print("Status: Error -", response.status_code, response.reason, "\n")

if __name__ == "main":
    test_page_url()

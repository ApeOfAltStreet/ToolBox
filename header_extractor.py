import requests

def get_http_headers(url):
    try:
        response = requests.get(url)
        headers = dict(response.headers)
        return headers
    except requests.RequestException as e:
        return {"error": str(e)}


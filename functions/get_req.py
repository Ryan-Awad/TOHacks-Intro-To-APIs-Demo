import requests
import json

def get_request(url):
    response = requests.get(url)
    response_code = response.status_code
    response_content = json.loads(response.content)
    return response_code, response_content
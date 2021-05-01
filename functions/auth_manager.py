import json

def get_api_key():
    with open('auth/api_key.json', mode='r') as api_key_json:
        api_key_json = json.loads(api_key_json.readline())
        api_key = api_key_json['api_key']
        return api_key
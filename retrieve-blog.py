# Use of the GET request

import json
from functions.auth_manager import get_api_key
from functions.get_req import get_request

api_key = get_api_key()

blog_id = input('Input the Blog ID of the blog you want to retrieve: ')
url = f'https://www.googleapis.com/blogger/v3/blogs/{blog_id}?key={api_key}'

response_code, response_content = get_request(url)

if response_code != 200:
    print("\n** SOMETHING WAS WRONG WITH YOUR REQUEST! **")

print(f'\nResponse Code: {response_code}')
print(f'\nResponse: {json.dumps(response_content, indent=4)}')

name = response_content['name']
desc = response_content['description']
posts_num = response_content['posts']['totalItems']
published_date = response_content['published']
updated_date = response_content['updated']

print('\n\n' + '-' * 50)
print(f'Blog name: {name}')
print(f'Description: {desc}')
print(f'Number of posts: {posts_num}')
print(f'Publication date: {published_date}')
print(f'Time of latest update: {updated_date}')
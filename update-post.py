# Use of the PUT request

import json
from google_auth_oauthlib.flow import InstalledAppFlow
from functions.auth_manager import get_api_key

api_key = get_api_key()

blog_id = input('Input the Blog ID of the blog where you want to edit a post: ')
post_id = input('Input the Post ID of the post you would like to edit: ')
title = input('Post title: ')
content = input('Post content (HTML supported): ')

flow = InstalledAppFlow.from_client_secrets_file(
    'auth/credentials.json',
    scopes=['https://www.googleapis.com/auth/blogger']
)

flow.run_local_server(
    authorization_prompt_message='Go through the OAuth process in the window that opened in your browser.',
    success_message='Successfully authenticated using OAuth.'
)

session = flow.authorized_session()

url = f'https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts/{post_id}?key={api_key}'

body = {
    "kind": "blogger#post",
    "id": blog_id,
    "blog": {
        "id": post_id
    },
    "title": title,
    "content": content
}

response = session.put(url, data=json.dumps(body))

response_code = response.status_code
response_content = json.loads(response.content)

if response_code != 200:
    print("\n** SOMETHING WAS WRONG WITH YOUR REQUEST! **")

print(f'\nResponse Code: {response_code}')
print(f'\nResponse: {json.dumps(response_content, indent=4)}')
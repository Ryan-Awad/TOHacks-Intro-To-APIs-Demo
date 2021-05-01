import json
from functions.api_key_manager import get_api_key
from functions.get_req import get_request

api_key = get_api_key()

blog_id = input('Input the Blog ID of the blog you want to retrieve: ')
url = f'https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts?key={api_key}'

response_code, response_content = get_request(url)

if response_code != 200:
    print("\n** SOMETHING WAS WRONG WITH YOUR REQUEST! **")

print(f'\nResponse Code: {response_code}')
print(f'\nResponse: {json.dumps(response_content, indent=4)}')

print('\n\n' + '-' * 100)

posts = response_content['items']
for (post, i) in zip(posts, range(len(posts))):
    title = post['title']
    content = post['content']
    comment_nums = post['replies']['totalItems']
    published_date = post['published']
    updated_date = post['updated']

    print(f'Post #{i+1}')
    print(f'Title: {title}')
    print(f'Content: {content}')
    print(f'Number of comments: {comment_nums}')
    print(f'Publication date: {published_date}')
    print(f'Time of latest update: {updated_date}')
    print('-' * 100)
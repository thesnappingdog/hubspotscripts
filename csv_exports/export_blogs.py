import requests
import csv
from config import Config


def get_blog_post_by_category(hapikey, content_group_id):
    params = {
        'hapikey': hapikey,
        'limit': '300',
        'content_group_id': content_group_id,
        'state': 'PUBLISHED'

    }
    return requests.get(Config.BLOG_POST_API, params=params).json()


def parse_blog_items(data, blogs):
    for item in data:
        blogs.append({
            'blog_id': item['id'],
            'name': item['name'],
            'url': item['absolute_url'],
            'topic_ids': item['topic_ids']
        })
    return blogs


def write_to_csv(blogs):
    with open(f'output/blogs.csv', 'w') as spreadsheet:
        fieldnames = ['blog_id', 'name', 'url', 'topic_ids']
        csv_writer = csv.DictWriter(spreadsheet, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(blogs)


if __name__ == "__main__":
    data = get_blog_post_by_category(Config.HAPIKEY, input('Content group ID: '))['objects']
    blogs = parse_blog_items(data, [])

    write_to_csv(blogs)
    print('OK')

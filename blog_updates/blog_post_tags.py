import requests
from config import Config


def get_all_blog_posts(hapikey):
    params = {
        'hapikey': hapikey,
        'limit': '300',
        'state': 'PUBLISHED'
    }
    return requests.get(Config.BLOG_POST_API, params=params).json()


def parse_blog_posts(blogs):
    blog_identifiers = []
    for blog in blogs:
        blog_identifiers.append({
            'blog_id': blog['id'],
            'name': blog['name'],
            'topic_ids': blog['topic_ids']
        })
    return blog_identifiers


def blog_operations(hapikey):
    return parse_blog_posts(get_all_blog_posts(hapikey)['objects'])


def get_topic_ids(hapikey):
    params = {
        'hapikey': hapikey,
        'limit': '500'
    }
    return requests.get(Config.BLOG_TOPIC_API, params=params).json()


def parse_topic_ids(topics):
    topic_identifiers = []
    for topic in topics:
        topic_identifiers.append({
            'topic_id': topic['id'],
            'name': topic['name'],
            'slug': topic['slug']
        })
    return topic_identifiers


def topic_id_operations(hapikey):
    return parse_topic_ids(get_topic_ids(hapikey)['objects'])


def blog_filter(blogs, keyword):
    blogs_f = []
    for blog in blogs:
        if keyword in blog['name']:
            blogs_f.append(blog)
    return blogs


if __name__ == "__main__":
    blogs = blog_operations(Config.HAPIKEY)
    topic_ids = topic_id_operations(Config.HAPIKEY)

    blogs_f = blog_filter(blogs, keyword=input('Keyword: '))
    for blog in blogs_f:
        print(blog['name'])



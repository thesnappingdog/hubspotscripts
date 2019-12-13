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
    blogs_to_update = []
    for blog in blogs:
        if keyword in blog['name'].upper():
            blogs_to_update.append(blog)
            print(blog['name'])
    return blogs_to_update


def choose_topic_id(topic_ids, keyword):
    for topic in topic_ids:
        if keyword in topic['name'].upper():
            print(topic)
            return topic


def replace_blog_topic(hapikey, blog_id, new_topic_id):
    json_body = {
        'topic_ids': [new_topic_id['topic_id']]
    }
    return requests.put(Config.BLOG_POST_API + blog_id, json=json_body, params=Config.generate_auth(hapikey))


def replace_blog_topics(hapikey, blogs_to_update, new_topic_id):
    for blog in blogs_to_update:
        response = replace_blog_topic(hapikey, blog['id'], new_topic_id)
        print(response)


def run_blog_tag_update():
    blogs = blog_operations(Config.HAPIKEY)
    topic_ids = topic_id_operations(Config.HAPIKEY)

    blogs_to_update = blog_filter(blogs, keyword=input('Blog Keyword: ').upper())
    new_topic_id = choose_topic_id(topic_ids, keyword=input('Topic Keyword: ').upper())

    checkpoint = input('Run update? Y/N: ').upper()
    if checkpoint == 'Y':
        replace_blog_topics(Config.HAPIKEY, blogs_to_update, new_topic_id)

    print('OK')





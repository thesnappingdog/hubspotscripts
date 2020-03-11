import requests
from config import Config


def get_relevant_blogs(hapikey, content_group):
    params = {'hapikey': hapikey, "content_group_id": content_group}
    return requests.get(Config.BLOG_POST_API, params=params).json()


def parse_blog_ids(raw, blogs):
    for blog in raw:
        blogs.append({
            'blog_id': blog['id'],
            'blog_name': blog['name']
        })
    return blogs


def build_json_body(author_id):
    return {"blog_author_id": str(author_id)}


def update_blog_author(hapikey, blog_id, author_id):
    res = requests.put(
        Config.BLOG_POST_API + str(blog_id),
        params=Config.generate_auth(hapikey),
        json=build_json_body(author_id)
    )
    print(res)


def update_all_blogs_author(hapikey, raw):
    author_id = input('New author ID: ')
    blogs = parse_blog_ids(raw, [])

    for blog in blogs:
        update_blog_author(hapikey, blog['blog_id'], author_id)


def run_update(hapikey):
    content_group = input('Content group ID: ')
    raw = get_relevant_blogs(hapikey, content_group)['objects']

    update_all_blogs_author(hapikey, raw)


if __name__ == "__main__":
    run_update(Config.HAPIKEY)






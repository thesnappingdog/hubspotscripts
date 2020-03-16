import requests
import csv
from config import Config


def load_csv_data(data):
    with open('./source/blog_example.csv', 'r') as sheet:
        raw = list(csv.DictReader(sheet))
        for i in raw:
            data.append({
                'blog_id': i['blog_id'],
                'topic_id': i['tags_final'].split(',')
            })
    return data


def update_blog_topic(hapikey, blog_id, topic_id):
    json = {'topic_ids': topic_id}
    return requests.put(Config.BLOG_POST_API + blog_id, json=json, params=Config.generate_auth(hapikey))


def loop_blog_topic_updates(data, hapikey):
    for blog in data:
        res = update_blog_topic(hapikey, blog['blog_id'], blog['topic_id'])
        print(res, blog['blog_id'])


if __name__ == "__main__":
    data = load_csv_data([])
    loop_blog_topic_updates(data, Config.HAPIKEY)

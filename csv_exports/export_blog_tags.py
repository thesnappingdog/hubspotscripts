import requests
import csv
from config import Config


def get_all_topic_ids(hapikey):
    params = {
        'hapikey': hapikey,
        'limit': 100
    }
    return requests.get(Config.BLOG_TOPIC_API, params=params).json()


def parse_topic_information(raw, topics):
    for topic in raw:
        topics.append({
            'topic_id': topic['id'],
            'name': topic['name'],
            'slug': topic['slug'],
            'description': topic['description']
        })
    return topics


def write_to_csv(topics):
    with open(f'./output/topics.csv', 'w') as spreadsheet:
        fieldnames = ['topic_id', 'name', 'slug', 'description']
        csv_writer = csv.DictWriter(spreadsheet, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(topics)


if __name__ == "__main__":
    raw = get_all_topic_ids(Config.HAPIKEY)['objects']
    topics = parse_topic_information(raw, [])
    write_to_csv(topics)
    print('Topics exported to topics.csv')


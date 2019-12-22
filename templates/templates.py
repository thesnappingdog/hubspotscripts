import requests
from config import Config


def get_all_templates(hapikey):
    return requests.get(Config.TEMPLATES_API, params=Config.generate_auth(hapikey)).json()


if __name__ == "__main__":
    templates = get_all_templates(Config.HAPIKEY)['objects']
    print(len(templates))
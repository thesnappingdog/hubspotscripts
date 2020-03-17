import requests
from config import Config

# Script will copy contact properties from a certain group. Script also assumes you have a
# company level group with the exact same name.


def get_contact_props(hapikey, group_name):
    params = {
        'hapikey': hapikey,
        'includeProperties': 'true'
    }
    return requests.get(Config.CONTACT_PROPS_GROUP_API + group_name, params=params).json()


def create_company_prop(hapikey, prop):
    del prop['hubspotDefined']
    return requests.post(Config.COMPANY_PROPS_API, json=prop, params=Config.generate_auth(hapikey))


def copy_all_group_props(hapikey, properties):
    for prop in properties:
        res = create_company_prop(hapikey, prop)
        print(res, prop['name'])


if __name__ == "__main__":
    properties = get_contact_props(Config.HAPIKEY, input('Contact Property Group API name: '))['properties']
    copy_all_group_props(Config.HAPIKEY, properties)
    print('OK DONE.')

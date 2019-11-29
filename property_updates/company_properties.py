import requests
from config import Config

# Request all company properties from one account, parse via Group name
# Change variable group to your own definition
# Make sure it's correct before running create_all_properties


def request_all_properties(hapikey):
    return requests.get(Config.COMPANY_PROPS_URL, params=Config.generate_auth(hapikey)).json()


def remove_immutable_keys(i):
    del i['hubspotDefined'], i['createdAt'], i['updatedAt'], i['createdUserId']
    return i


def prepare_properties(data, group):
    properties = []
    for i in data:
        if group in i['groupName']:
            properties.append(remove_immutable_keys(i))
    return properties


def create_property(hapikey, property):
    return requests.post(Config.COMPANY_PROPS_URL, json=property, params=Config.generate_auth(hapikey))


def create_all_properties(hapikey, properties):
    for property in properties:
        response = create_property(hapikey, property)
        print(response)


def run_company_property_update():
    data = request_all_properties(Config.HAPIKEY_SAND)
    group = str(input('API name of properties group: '))
    properties = prepare_properties(data, group)
    create_all_properties(Config.HAPIKEY, properties)


import requests
from config import Config


def request_all_properties():
    return requests.get(Config.COMPANY_PROPS_URL, params=Config.HAPIKEY_SAND).json()


def parse_properties(data, group):
    properties = []
    for i in data:
        if group in i['groupName']:
            del i['hubspotDefined']
            del i['createdAt']
            del i['updatedAt']
            del i['createdUserId']
            properties.append(i)
    return properties


def create_property(property):
    return requests.post(Config.COMPANY_PROPS_URL, json=property, params=Config.HAUTH_PROD)


def create_all_properties(properties):
    for property in properties:
        response = create_property(property)
        print(response)


if __name__ == "__main__":
    data = request_all_properties()
    group = 'data_infrastructure'
    properties = parse_properties(data, group)
    create_all_properties(properties)


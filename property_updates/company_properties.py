import requests
from config import Config


def request_all_properties():
    params = {'hapikey': Config.HAPIKEY_SAND}
    return requests.get(Config.COMPANY_PROPS_URL, params=params).json()


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
    params = {'hapikey': Config.HAPIKEY}
    return requests.post(Config.COMPANY_PROPS_URL, json=property, params=params)


def create_all_properties(properties):
    for property in properties:
        response = create_property(property)
        print(response)


if __name__ == "__main__":
    data = request_all_properties()
    group = 'data_infrastructure'
    properties = parse_properties(data, group)
    #print(properties[0])
    create_all_properties(properties)


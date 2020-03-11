import requests
import csv
from config import Config

# This script is used to map single-field country (clearbit) values to an enumerated (dropdown) field
# Data comes from a CSV. See ./source for a example.
# To change which property is looked at, switch property in the filters below.


def generate_last_action(country):
    return {
        "type": "BRANCH",
        "filters": [
            [
                {
                    "operator": "EQ",
                    "value": country['cb_country'],
                    "property": "clearbit_country_of_person",
                    "type": "string"

                }
            ]
        ],
        "acceptActions": [
            {
                "type": "SET_CONTACT_PROPERTY",
                "propertyName": "country",
                "newValue": country['hs_country'],
            }
        ],
        "rejectActions": []
    }


def generate_actions_body(countries, action):
    for country in countries[0:14]:
        action = {
            "type": "BRANCH",
            "filters": [
                [
                    {
                        "operator": "EQ",
                        "value": country['cb_country'],
                        "property": "clearbit_country_of_person",
                        "type": "string"

                    }
                ]
            ],
            "acceptActions": [
                {
                    "type": "SET_CONTACT_PROPERTY",
                    "propertyName": "country",
                    "newValue": country['hs_country'],
                }
            ],
            "rejectActions": [action]
        }

    return [action]


def load_countries(countries):
    with open('source/example.csv', 'r') as sheet:
        raw = list(csv.DictReader(sheet))
        for country in raw:
            countries.append({
                "cb_country": country['cb_country'],
                "hs_country": country['hs_country'],
            })
    return countries


def create_new_workflow(hapikey, new_flow_body):
    return requests.post(Config.WORKFLOWS_API, json=new_flow_body, params=Config.generate_auth(hapikey))


def build_post_body(action_body, name):
    return {
        "name": name,
        "type": "DRIP_DELAY",
        "onlyEnrollsManually": 'true',
        "actions": action_body
    }


# This is just bad practice. Fix it later when you have time.

def manual_loop_workflows_set1(hapikey, countries):
    action = generate_last_action(countries[0])
    action_body = generate_actions_body(countries[1:14], action)
    new_flow_body = build_post_body(action_body, "Workflow 1")

    return create_new_workflow(hapikey, new_flow_body)


def manual_loop_workflows_set2(hapikey, countries):
    action = generate_last_action(countries[15])
    action_body = generate_actions_body(countries[16:], action)
    new_flow_body = build_post_body(action_body, "Workflow 2")

    return create_new_workflow(hapikey, new_flow_body)


if __name__ == "__main__":

    countries = load_countries([])
    res1 = manual_loop_workflows_set1(Config.HAPIKEY, countries)
    print(res1)
    res2 = manual_loop_workflows_set2(Config.HAPIKEY, countries)
    print(res2)

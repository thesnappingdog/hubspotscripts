import requests, csv
from config import Config


def get_all_workflows(hapikey):
    return requests.get(Config.WORKFLOWS_API, params=Config.generate_auth(hapikey)).json()


def filter_inactive_workflows(workflows):
    inactive_flows = []
    for workflow in workflows:
        if not workflow['enabled']:
            inactive_flows.append(workflow)
    return inactive_flows


def filter_flows_to_keep(inactive_flows, keyword):
    delete_list = []
    for flow in inactive_flows:
        if keyword not in flow['name'].upper():
            delete_list.append(flow)
    return delete_list


def delete_workflow_request(hapikey, flow_id):
    return requests.delete(Config.WORKFLOWS_API + flow_id, params=Config.generate_auth(hapikey))


def bulk_delete_workflows(hapikey, deletion_list):
    for flow in deletion_list:
        print(delete_workflow_request(hapikey, str(flow['id'])))


def run_bulk_delete_workflows():
    workflows = get_all_workflows(Config.HAPIKEY)['workflows']
    inactive_flows = filter_inactive_workflows(workflows)

    delete_list = filter_flows_to_keep(inactive_flows, keyword=input('Keyword: ').upper())
    bulk_delete_workflows(Config.HAPIKEY, delete_list)


if __name__ == "__main__":
    run_bulk_delete_workflows()
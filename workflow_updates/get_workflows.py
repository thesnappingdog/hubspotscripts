import requests
from config import Config


def get_all_workflows():
    return requests.get(Config.WORKFLOWS_URL, params=Config.HAUTH_SAND).json()


def parse_workflow_ids(workflows):
    workflow_ids = []
    for workflow in workflows['workflows']:
        workflow_ids.append({'workflow_id': workflow['id']})
    return workflow_ids


def get_single_workflow(workflow_id):
    url = f'{Config.WORKFLOWS_URL}{workflow_id}'
    workflow_data = requests.get(url, Config.HAUTH_SAND).json()
    return workflow_data


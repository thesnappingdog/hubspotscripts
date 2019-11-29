import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    HAPIKEY = os.environ.get('HAPIKEY_MAIN')
    HAPIKEY_SAND = os.environ.get('HAPIKEY_SAND')

    FLOW_BASE_URL = "https://api.hubapi.com/automation/v3/workflows/"
    COMPANY_PROPS_URL = "https://api.hubapi.com/properties/v1/companies/properties/"
    FORM_API_URL = "https://api.hubapi.com/forms/v2/forms/"

    @staticmethod
    def generate_auth(hapikey):
        return {'hapikey': hapikey}

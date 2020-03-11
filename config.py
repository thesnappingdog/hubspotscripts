import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    HAPIKEY = os.environ.get('HAPIKEY_MAIN')
    HAPIKEY_SAND = os.environ.get('HAPIKEY_SAND')

    WORKFLOWS_API = "https://api.hubapi.com/automation/v3/workflows/"
    COMPANY_PROPS_API = "https://api.hubapi.com/properties/v1/companies/properties/"
    CONTACT_PROPS_API = "https://api.hubapi.com/properties/v1/contacts/properties/"
    CONTACT_PROPS_API_NAMED = CONTACT_PROPS_API + "named/"
    FORMS_API = "https://api.hubapi.com/forms/v2/forms/"
    BLOG_POST_API = "https://api.hubapi.com/content/api/v2/blog-posts/"
    BLOG_TOPIC_API = "https://api.hubapi.com/blogs/v3/topics/"
    MARKETING_EMAIL_API = "https://api.hubapi.com/marketing-emails/v1/emails/"
    TEMPLATES_API = "http://api.hubapi.com/content/api/v2/templates/"
    LISTS_API = "https://api.hubapi.com/contacts/v1/lists/"

    @staticmethod
    def generate_auth(hapikey):
        return {'hapikey': hapikey}

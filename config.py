import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    HAPIKEY_MAIN = os.environ.get('HAPIKEY_MAIN')
    HAPIKEY_SAND = os.environ.get('HAPIKEY_SAND')



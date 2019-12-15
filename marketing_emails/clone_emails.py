import requests
import pandas as pd
from config import Config


def get_template_email(hapikey, email_id):
    return requests.get(Config.MARKETING_EMAIL_API + email_id, params=Config.generate_auth(hapikey)).json()


def get_sheet_information(sheet_url):
    response = requests.get(sheet_url).content
    return pd.read_csv(response)


if __name__ == "__main__":
    #template_email = get_template_email(Config.HAPIKEY, email_id=input('Email id: '))
    sheet_information = get_sheet_information(sheet_url=input('Sheet URL: '))

    print(sheet_information)

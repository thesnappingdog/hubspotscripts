import requests
from config import Config


# Groundwork - get all forms, select which ones to update.

def get_all_forms(hapikey):
    return requests.get(Config.FORMS_API, params=Config.generate_auth(hapikey)).json()


def get_template_form(hapikey, form_id):
    return requests.get(Config.FORMS_API + form_id, params=Config.generate_auth(hapikey)).json()


def prepare_form_operations(keyword):
    forms = get_all_forms(Config.HAPIKEY)
    forms_to_update = filter_form_by_name(forms, keyword)
    return forms_to_update


# These keys need to be included into form update body

def list_all_form_constants(forms):
    form_constants = []
    for form in forms:
        form_constants.append({
            'form_id': form['guid'],
            'name': form['name'],
            'submitText': form['submitText'],
            'redirect': form['redirect'],
            'notifyRecipients': form['notifyRecipients']
        })
    return form_constants


def list_single_form_constants(form):
    form_constants = {
        'form_id': form['guid'],
        'name': form['name'],
        'submitText': form['submitText'],
        'redirect': form['redirect'],
        'notifyRecipients': form['notifyRecipients']
    }
    return form_constants


# Build JSON body for PUT request.

def build_form_update_body(form_template, form_constant):
    form_body = {
        'name': form_constant['name'],
        'redirect': form_constant['redirect'],
        'submitText': form_constant['submitText'],
        'notifyRecipients': form_constant['notifyRecipients'],
        "formFieldGroups": form_template['formFieldGroups']
    }
    return form_body


# Update bulk or single forms with functions below.

def update_single_form(hapikey, form_id, form_body):
    return requests.put(
        Config.FORMS_API + form_id,
        json=form_body,
        params=Config.generate_auth(hapikey)
    )


def bulk_update_forms(forms_to_update, form_template):
    for form in forms_to_update:
        form_constants = list_single_form_constants(form)
        form_body = build_form_update_body(form_template, form_constants)
        print(form_body)

        response = update_single_form(Config.HAPIKEY, form_constants['form_id'], form_body)
        print(f"{response} for {form_constants['form_id']}")


# Utilities // Find forms you're looking for.

def filter_form_by_name(forms, name):
    forms_to_update = []
    for form in forms:
        if name.upper() in form['name'].upper():
            forms_to_update.append(form)
    return forms_to_update


def filter_form_by_id(forms, form_id):
    forms_to_update = []
    for form in forms:
        if form_id in form['guid']:
            forms_to_update.append(form)
    return forms_to_update


if __name__ == "__main__":
    keyword = input('TYPE IN KEYWORD OR NAMING CONVENTION FOR YOUR FORMS: ')
    forms_to_update = prepare_form_operations(keyword.upper())
    form_constants = list_all_form_constants(forms_to_update)

    # '04ab40ce-6f56-46d1-91c6-46f5d611c9ca'
    print('##########################################')
    print('GO TO YOUR FORM, COPY FORM ID FROM THE URL')
    print('PASTE YOUR TEMPLATE FORM ID HERE. THIS PART IS CASE SENSITIVE')
    print('##########################################')
    form_id = input('FORM ID: ')

    form_template = get_template_form(Config.HAPIKEY, form_id)
    bulk_update_forms(forms_to_update, form_template)
    
    
    





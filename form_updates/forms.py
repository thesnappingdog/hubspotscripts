import requests
from config import Config


# Groundwork - get all forms, select which ones to update.

def get_all_forms(hapikey):
    return requests.get(Config.FORMS_API, params=Config.generate_auth(hapikey)).json()


def get_template_form(hapikey, form_id):
    return requests.get(Config.FORMS_API + form_id, params=Config.generate_auth(hapikey)).json()


def prepare_form_operations(hapikey, keyword):
    forms = get_all_forms(hapikey)
    forms_to_update = filter_form_by_name(forms, keyword)
    return forms_to_update


# These keys need to be included into form update body

def parse_form_constants(form):
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

def bulk_update_forms(forms_to_update, form_template):
    for form in forms_to_update:
        form_constants = parse_form_constants(form)
        form_body = build_form_update_body(form_template, form_constants)

        response = update_single_form(Config.HAPIKEY, form_constants['form_id'], form_body)
        print(f"{response} for {form_constants['form_id']}")


def update_single_form(hapikey, form_id, form_body):
    return requests.put(
        Config.FORMS_API + form_id,
        json=form_body,
        params=Config.generate_auth(hapikey)
    )


# Utilities // Find forms you're looking for.
# Get form by ID is not used, but can be handy if you want to
# Filter by ID rather than name.

def filter_form_by_name(forms, keyword):
    forms_to_update = []
    for form in forms:
        if keyword in form['name'].upper():
            forms_to_update.append(form)
            print(form['name'])
    return forms_to_update


def filter_form_by_id(forms, form_id):
    forms_to_update = []
    for form in forms:
        if form_id in form['guid']:
            forms_to_update.append(form)
    return forms_to_update


def run_form_updates(hapikey):
    keyword = input('TYPE IN KEYWORD OR NAMING CONVENTION FOR YOUR FORMS: ')
    forms_to_update = prepare_form_operations(hapikey, keyword.upper())

    print('GO TO YOUR FORM, COPY FORM ID FROM THE URL')
    print('PASTE YOUR TEMPLATE FORM ID HERE. THIS PART IS CASE SENSITIVE')

    form_id = input('FORM ID: ')
    form_template = get_template_form(hapikey, form_id)
    print(f"Is this your template: {form_template['name']} ?")

    #bulk_update_forms(forms_to_update, form_template)


if __name__ == "__main__":
    run_form_updates()

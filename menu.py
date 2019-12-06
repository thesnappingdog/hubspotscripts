from config import Config
from form_updates import forms as forms
from property_updates import company_properties as comp


def welcome():
    print('# # # # # # # # # # # # # # # # # #')
    print('\nWelcome to Hubspot Scripts\n')
    print('If something goes wrong, the script will simply shutdown.\nJust run it again if that happens.\n')
    print('# # # # # # # # # # # # # # # # # #')


def options():
    print('\nTo select an option, simply type in the number\n')
    print('1 - Bulk Update Forms Script\n2 - Copy Company Properties')
    print('3 - Exit program\n')
    option = input('Selection: ')
    return option


def script_selector(option):
    if option == '1':
        forms.run_form_updates(Config.HAPIKEY)
    elif option == '2':
        comp.run_company_property_update()
    else:
        print('Program terminated.')


def main_menu():
    welcome()
    option = options()
    script_selector(option)


if __name__ == "__main__":
    main_menu()
from config import Config
import form_updates.forms as forms

if __name__ == "__main__":
    forms.run_form_updates(Config.HAPIKEY)

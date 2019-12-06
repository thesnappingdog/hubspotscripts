# HUBSPOT SCRIPTS 0.5
This repo contains useful scripts for doing bulk operations in Hubspot.

Current collection:

- Update Forms in bulk
- Copy company properties from one portal to another

## Installation

Run the following command in root directory:

```pipenv install```

Create a `.env` file in the root directory:

```
HAPIKEY_MAIN=your_hubspot_api_key
HAPIKEY_SAND=optional_additional_key_if_needed
```

## Usage

The scripts are used from the Terminal. No clickedy click interface coming.

To start, run the following:

```pipenv run python menu.py```

Select an option and follow the script's instructions


## Upcoming scripts

- Bulk create marketing emails with CSV data and a template
- Bulk create contact workflows with CSV data and a template
- Feel free to suggest ideas :)


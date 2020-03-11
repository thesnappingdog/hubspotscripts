# HUBSPOT SCRIPTS 0.5
This repo contains useful scripts for doing bulk operations in Hubspot.

Updated collection:

- Update Forms in bulk (via menu)
- Copy company properties from one portal to another (via menu)
- Delete contact workflows in bulk (check script)

New additions: 

- Update selected blog post Topic IDs (via menu)
- Export blog post tags aka topic IDs to CSV (check script)
- Export Blog post metadata - id, name, url, topic ids (check script
- Update blog post author in bulk (check script)
- Create a workflow with 15 if branches based on CSV data =>  This one is specifically made for mapping clearbit countries to enumarated country values, but might make this more generic if it turns out to be useful


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


import os
import json
import gspread
from google.oauth2 import service_account

def publish_to_google_sheets():
    # Debug statement to check the value of the environment variable
    print("Environment Variable - GOOGLE_SERVICE_ACCOUNT_KEY:", os.getenv('GOOGLE_SERVICE_ACCOUNT_KEY'))

    # Get the value of the environment variable
    creds_json = os.getenv('GOOGLE_SERVICE_ACCOUNT_KEY')

    # Check if the variable is not None
    if creds_json is None:
        print("Error: GOOGLE_SERVICE_ACCOUNT_KEY environment variable is not set.")
        return

    # Check if the variable is an empty string
    if not creds_json.strip():
        print("Error: GOOGLE_SERVICE_ACCOUNT_KEY environment variable is empty.")
        return

    try:
        creds_dict = json.loads(creds_json)
        # Rest of your code here
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)

if __name__ == '__main__':
    publish_to_google_sheets()


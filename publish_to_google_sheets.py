import os
import json  # Import the json module
import gspread
from google.oauth2 import service_account

def publish_to_google_sheets():
    # Authenticate using the service account key stored in GitHub Secrets
    creds_dict = json.loads(os.getenv('GOOGLE_SERVICE_ACCOUNT_KEY'))
    creds = service_account.Credentials.from_service_account_info(creds_dict)
    client = gspread.authorize(creds)

    # Open the Google Sheet by its ID
    sheet = client.open_by_key("1sRAHtxVFm87uoYI-dYCmrgpq1hZaBmHz-1M-EgR5eFk").sheet1

    # Example: Update cell A1 with "Hello, World!"
    sheet.update("A1", "Hello, World!")

if __name__ == "__main__":
    publish_to_google_sheets()

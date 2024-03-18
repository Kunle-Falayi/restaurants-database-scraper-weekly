import gspread
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
import os
import json

def publish_to_google_sheets():
    # Load the Google service account key from environment variable
    creds_dict = json.loads(os.getenv('GOOGLE_SERVICE_ACCOUNT_KEY'))

    # Create a Google Credentials object
    creds = Credentials.from_service_account_info(creds_dict)

    # Authorize the client
    client = gspread.authorize(creds)

    # Open the Google Sheets document by its title
    sheet = client.open('Your Google Sheets Document Title').sheet1

    # Example: Write data to a specific cell
    sheet.update('A1', 'Hello, Google Sheets!')

if __name__ == "__main__":
    publish_to_google_sheets()

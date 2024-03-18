import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def publish_to_google_sheets():
    # Load the Google Service Account Key from the environment
    key_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    
    # Load the credentials from the JSON file
    with open(key_path, 'r') as key_file:
        creds_dict = json.load(key_file)

    # Define the scope for Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    # Authenticate using the Service Account Credentials
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

    # Authorize the client
    client = gspread.authorize(creds)

    # Access the Google Sheets spreadsheet by its title
    spreadsheet = client.open('Your Spreadsheet Title')

    # Access the specific worksheet by its title
    worksheet = spreadsheet.worksheet('Sheet1')

    # Example: Update a cell with a value
    worksheet.update('A1', 'Hello, Google Sheets!')

    # Example: Append rows to the worksheet
    data = [['John', 25], ['Jane', 30], ['Doe', 28]]
    worksheet.append_rows(data)

    print("Data published to Google Sheets successfully!")

if __name__ == "__main__":
    publish_to_google_sheets()

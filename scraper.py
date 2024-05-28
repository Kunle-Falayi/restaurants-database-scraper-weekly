import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime, timedelta
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import os
import json

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Load credentials from environment variable
credentials_json = os.environ.get('GOOGLE_SHEETS_CREDENTIALS')
creds_dict = json.loads(credentials_json)

# Add your service account file
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

# Authorize the clientsheet 
client = gspread.authorize(creds)

# Get the Google Sheet
sheet = client.open('Restaurant_inspection_database(auto_scraper)').sheet1

# Scraper logic
base_url = "http://envapp.maricopa.gov/EnvironmentalHealth/FoodGrade?"
today = datetime.now()
days_to_friday = (today.weekday() - 4) % 7
last_friday = today - timedelta(days=days_to_friday)
friday_date_str = last_friday.strftime("%m/%d/%Y")
full_url = f"{base_url}d={friday_date_str}&a=true"

url = urlopen(full_url)
soup_doc = bs(url, "html.parser")
table = soup_doc.find_all("tr")

master_data = []

for row in table[1:]:  # skip the first row, it contains headers
    rest_list = row.find_all('td')
    inspection_link = row.find('td', {'class': 'boldTextCenter'}).a['href']
    list_headers = ['Business Name', 'Address', 'City', 'Permit_ID', 'Type', 'Class', 'Inspection_Date', 'Inspection_Type', 'Grade', 'Priority_Violations', 'CuttingEdge', 'Inspection_Details']
    rest_data = []
    for index, col in enumerate(rest_list):
        rest_data.append(col.text)
    rest_data.append('http://envapp.maricopa.gov' + inspection_link)
    rest_dict = dict(zip(list_headers, rest_data))
    master_data.append(rest_dict)

pd.option_context('display.max_colwidth', None)
df = pd.DataFrame(master_data)
df = df[['Business Name', 'Address', 'City', 'Permit_ID', 'Type', 'Class', 'Inspection_Date', 'Inspection_Type', 'Grade', 'Priority_Violations', 'Inspection_Details']]

# Convert DataFrame to list of lists
data_list = df.values.tolist()

# Update the Google Sheet with the data
sheet.update('A1', [df.columns.values.tolist()] + data_list)

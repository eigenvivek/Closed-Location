# Import necessary Google API and time packages
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta
import time
import config
import json
import requests

# Traker class to manage variables and functions
class Tracker:

    # Initialize the tracker
    def __init__(self):

        # Enable main.py to access Google spreadsheets
        self.scope = scope = ['https://spreadsheets.google.com/feeds',
                              'https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',self.scope)
        self.client = gspread.authorize(self.creds)

        # Open sheet
        self.sheet = self.client.open('location-data').sheet1
        self.index = 2

        # Import ipstack key
        self.key = config.ipstack_key
        self.send_url = 'http://api.ipstack.com/check?access_key={}'.format(self.key)

        # If the first row is empty, add the header
        if self.sheet.acell('A1').value=='':
            self.make_header()

        # Update settings
        self.delta = timedelta(minutes=15)

    # Make header
    def update_sheet(self):
        r = requests.get(self.send_url)
        j = json.loads(r.text)
        row = [list(j.keys())[index] for index in [0,3,5,6,8,9,10,11]]
        row.insert(0, 'time')
        self.sheet.insert_row(row, 1)

    # Get location information and update sheet
    def update_sheet(self):

        # Request location information from ipstack API
        r = requests.get(self.send_url)
        j = json.loads(r.text)

        # Isolate desired data
        important_data = [0,3,5,6,8,9,10,11]
        row = [j[list(j.keys())[index]] for index in important_data]

        # Insert time
        row.insert(0, str(datetime.now()))

        # Update
        self.sheet.insert_row(row, self.index)

    # Main function
    def main(self):
        self.update_sheet()
        # starttime = datetime.now()
        # update_time = starttime + self.delta
        #
        # if datetime.now() < update_time:
        #     for i in range(60):
        #         time.sleep(1)
        # else:
        #     self.update_sheet()


if __name__ == "__main__":
    tracker = Tracker()
    tracker.main()

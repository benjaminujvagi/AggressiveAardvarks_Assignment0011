# zip code.py
# Brief Description of what this module does. calls a function to fill in missing zip codes in data. 
# Citations: Microsoft copilot

import requests
import pandas as pd

class ZipFiller:
    def __init__(self, api_key):
        self.api_key = api_key

    def fill_missing_zip_codes(self, data):
        for index, row in data.iterrows():
            if pd.isnull(row['Full Address']):
                city = row['City']
                response = requests.get(
                    f'https://app.zipcodebase.com/api/v1/search?apikey={self.api_key}&city={city}&country=US'
                )
                if response.status_code == 200:
                    zip_code = response.json()['results'][city][0]['postal_code']
                    data.at[index, 'Full Address'] = zip_code
        return data

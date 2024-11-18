# cleaned.py

import pandas as pd

class DataCleaner:
    """
    A class for cleaning and formatting data in a pandas DataFrame.
    param input: csv file
    return cleaned data
    """
    def __init__(self, data):
        self.data = data

    def format_gross_price(self):
        self.data['Gross Price'] = self.data['Gross Price'].apply(lambda x: f"{float(x):.2f}")

    def remove_duplicates(self):
        self.data.drop_duplicates(inplace=True)

    def get_data(self):
        return self.data

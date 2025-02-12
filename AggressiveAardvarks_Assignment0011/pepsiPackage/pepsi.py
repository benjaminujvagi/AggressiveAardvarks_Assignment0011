# Brief Description of what this module does. This module cleans errant pepsi entries in the fuel data sheet and relocates them to the data anomalies sheet
# Citations: none
# Anything else that's relevant: NA


import pandas as pd

class AnomalyHandler:
    def __init__(self, data):
        self.data = data

    def separate_anomalies(self):
        anomalies = self.data[self.data['Fuel Type'] == 'Pepsi']
        cleaned_data = self.data[self.data['Fuel Type'] != 'Pepsi']
        return cleaned_data, anomalies

    def save_anomalies(self, dataAnomalies, file_path):
        dataAnomalies.to_csv(file_path, index=False)
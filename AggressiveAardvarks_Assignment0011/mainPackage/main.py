#main.py
# Name: Ben Ujvagi, Jacob Shultze, Danny Barnhouse, Dobry Shaw
# email:  ujvagibw@mail.uc.edu, schul2jt@mail.uc.edu, barnhodw@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:  11/21/2024
# Course #/Section:  IS4010-001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: imported data and cleaned it up
# Brief Description of what this module does. In this module, we call everything together 
# Citations: Microsoft Copilot
from cleanedPackage.cleaned import DataCleaner
from zipcodePackage.zipcode import ZipFiller
from pepsiPackage.pepsi import AnomalyHandler
import pandas as pd

def main():
    file_path = 'dataPackage/fuelPurchaseData.csv'
    cleaned_file_path = 'dataPackage/cleanedData.csv'
    anomaly_file_path = 'dataPackage/dataAnomalies.csv'
    api_key = 'f3f2eab0-a0fa-11ef-ba9f-554a75d8092e'

    # Load data
    data = pd.read_csv(file_path, low_memory=False)
    try:

        # Initialize cleaner
        cleaner = DataCleaner(data)
        cleaner.format_gross_price()
        cleaner.remove_duplicates()
        cleaned_data = cleaner.get_data()

        # Handle anomalies
        anomaly_handler = AnomalyHandler(cleaned_data)
        cleaned_data, anomalies = anomaly_handler.separate_anomalies()
        anomaly_handler.save_anomalies(anomalies, anomaly_file_path)

        # Print the anomalies to verify 
        print(f"Anomalies saved to {anomaly_file_path}:") 
        print(anomalies)

        # Fill missing zip codes
        zip_filler = ZipFiller(api_key)
        cleaned_data = zip_filler.fill_missing_zip_codes(cleaned_data)

        # Save the cleaned data
        cleaner = DataCleaner(cleaned_data)
        cleaner.save_cleaned_data(cleaned_file_path)

        # Print the cleaned data to verify 
        print(f"Cleaned data saved to {cleaned_file_path}:") 
        print(cleaned_data)

    except ValueError as e: 
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
   


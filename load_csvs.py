import os
import pandas as pd

# Path to your DATA folder
data_folder = r"C:\Users\hp\Desktop\CW2_M01057432_CST1510\DATA"

# Ensure DATA folder exists
if not os.path.exists(data_folder):
    os.makedirs(data_folder)
    print(f"📁 Created missing folder: {data_folder}")
else:
    print(f"📁 DATA folder found: {data_folder}")

# List of CSV files to load
files = ["datasets_metadata.csv", "it_tickets.csv", "cyber_incidents.csv"]

# Dictionary to store loaded DataFrames
dataframes = {}

# Check each file and load if it exists
for file_name in files:
    file_path = os.path.join(data_folder, file_name)
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        dataframes[file_name] = df
        print(f"✅ Loaded {file_name}, rows: {len(df)}")
    else:
        print(f"❌ Missing: {file_name}. Please add this file to {data_folder}.")

# Example of how to access your loaded data
# datasets_metadata_df = dataframes.get("datasets_metadata.csv")
# it_tickets_df = dataframes.get("it_tickets.csv")
# cyber_incidents_df = dataframes.get("cyber_incidents.csv")

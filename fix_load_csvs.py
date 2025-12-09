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

# CSV files and their headers (adjust headers as needed)
csv_files = {
    "datasets_metadata.csv": ["id", "name", "description"],
    "it_tickets.csv": ["ticket_id", "title", "status"],
    "cyber_incidents.csv": ["incident_id", "type", "severity"]
}

# Dictionary to store loaded DataFrames
dataframes = {}

# Check each file, create if missing, then load
for file_name, headers in csv_files.items():
    file_path = os.path.join(data_folder, file_name)
    
    # Create empty CSV if missing
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=headers)
        df.to_csv(file_path, index=False)
        print(f"📝 Created missing file: {file_name} with headers {headers}")
    else:
        df = pd.read_csv(file_path)
        print(f"✅ Loaded {file_name}, rows: {len(df)}")
    
    dataframes[file_name] = df

# Access your DataFrames like this:
datasets_metadata_df = dataframes["datasets_metadata.csv"]
it_tickets_df = dataframes["it_tickets.csv"]
cyber_incidents_df = dataframes["cyber_incidents.csv"]

# Example: print first 5 rows
print(datasets_metadata_df.head())

import os
import pandas as pd
import sqlite3

# Paths
data_folder = r"C:\Users\hp\Desktop\CW2_M01057432_CST1510\DATA"
db_path = os.path.join(data_folder, "intelligence_platform.db")

# Ensure DATA folder exists
if not os.path.exists(data_folder):
    os.makedirs(data_folder)
    print(f"📁 Created missing folder: {data_folder}")

# CSV files to load
csv_files = [
    "datasets_metadata.csv",
    "it_tickets.csv",
    "cyber_incidents.csv"
]

# Connect to SQLite database
conn = sqlite3.connect(db_path)

for file_name in csv_files:
    file_path = os.path.join(data_folder, file_name)
    
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        
        # Table name same as file name without extension
        table_name = os.path.splitext(file_name)[0]
        
        # Create or replace table automatically
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"✅ Loaded {file_name} into table '{table_name}', rows: {len(df)}")
    else:
        print(f"❌ Missing file: {file_name}. Please add it to {data_folder}")

# Close database connection
conn.close()

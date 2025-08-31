import pandas as pd
import os

# Creating a sample DataFrame with column names
data = { 'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35],
         'City': ['New York', 'Los Angeles', 'Chicago'] }

df = pd.DataFrame(data)

# Adding a new record into dataFrame V2

new_record = {'Name': 'GF1', 'Age': 28, 'City': 'San Francisco'}
df.loc[len(df.index)] = new_record

new_record2 = {'Name': 'GF2', 'Age': 28, 'City': 'France'}
df.loc[len(df.index)] = new_record2

# Ensure the "data" directory is in root
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Save the DataFrame to a CSV file in the "data" directory
csv_file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(csv_file_path, index=False)
print(f"DataFrame saved to {csv_file_path}")

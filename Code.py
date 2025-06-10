import pandas as pd
import os

# Create a sample DataFrame with colmn names
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
        }

df = pd.DataFrame(data)

# Adding new row to df for v2
# new_row_loc = {'Name':'V2','Age':20,'City':'City1'}
# df.loc[len(df)] = new_row_loc

# Adding new row to df for v3
# new_row_loc2 = {'Name': 'V3', 'Age': 30, 'City': 'City1'}
# df.loc[len(df)] = new_row_loc2

# Ensure the 'data' directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file, including column names
df.to_csv(file_path, index=False)

# Print the DataFrame to verify
print("DataFrame saved to:", file_path)
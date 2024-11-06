import os
import pandas as pd

# Define folder path containing the cleaned CSV files
folder_path = './data pre-processing/cleaned_unrelated_pics'

# Initialize variables to store counts and filenames
row_counts = {}
total_rows = 0

# Loop through each CSV file in the folder
for csv_file in os.listdir(folder_path):
    if csv_file.endswith(".csv"):
        file_path = os.path.join(folder_path, csv_file)

        # Load CSV and count rows (excluding header)
        data = pd.read_csv(file_path)
        row_count = len(data)

        # Update counts
        row_counts[csv_file] = row_count
        total_rows += row_count

# Calculate minimum and maximum row counts
min_rows = min(row_counts.values())
max_rows = max(row_counts.values())

# Display results
print("Row count per file:")
for file_name, count in row_counts.items():
    print(f"{file_name}: {count} rows")

print(f"\nOverall total rows across all files: {total_rows}")
print(f"Minimum number of rows in a file: {min_rows}")
print(f"Maximum number of rows in a file: {max_rows}")

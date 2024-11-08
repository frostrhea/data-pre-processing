import pandas as pd
import os
import requests

input_folder = "D:/Documents/4th year files/CSC173/filipino_food_calories/filipino-food-classifier/notebooks/data/filipino_food"
output_folder = ".\data pre-processing\cleaned_invalid_links"
os.makedirs(output_folder, exist_ok=True)


def is_valid_url(url):
    try:
        # Make a HEAD request to save time
        response = requests.head(url, timeout=5)
        return response.status_code == 200  # Valid if status is 200 (OK)
    except requests.RequestException:
        return False


# Loop through all CSV files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_folder, filename)

        # Load data and remove duplicates
        data = pd.read_csv(file_path)
        original_count = len(data)
        cleaned_data = data.drop_duplicates()

        # Filter rows with valid URLs only
        cleaned_data = cleaned_data[cleaned_data.iloc[:, 0].apply(
            is_valid_url)]

        # Save cleaned data
        cleaned_file_path = os.path.join(output_folder, filename)
        cleaned_data.to_csv(cleaned_file_path, index=False)

        cleaned_count = len(cleaned_data)
        print(
            f"{filename}: {original_count} entries -> {cleaned_count} valid entries after cleaning.")

import os
import pandas as pd
import requests
from tqdm import tqdm
import re

csv_folder = './data pre-processing/cleaned_unrelated_pics - Copy'
download_folder = './data pre-processing/downloaded_imgs_new'

os.makedirs(download_folder, exist_ok=True)

# Function to sanitize food names for use in filenames


def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '', name).replace(' ', '_')


# Initialize a global counter for image naming
image_counter = 1

# Loop through all CSV files in the specified folder
for csv_file in os.listdir(csv_folder):
    if csv_file.endswith('.csv'):
        # Read the CSV file without headers
        df = pd.read_csv(os.path.join(csv_folder, csv_file), header=None)

        # Loop through each row in the DataFrame
        for index, row in tqdm(df.iterrows(), total=df.shape[0]):
            # Extract the URL and food name (assuming the columns are positional)
            url = row[0]
            food_name = sanitize_filename(row[1])  # Sanitize food name

            food_folder = os.path.join(download_folder, food_name)
            os.makedirs(food_folder, exist_ok=True)

            try:
                # Download the image
                response = requests.get(url, timeout=5)
                response.raise_for_status()

                # Generate a filename for the image (e.g., image_1.jpg)
                image_filename = os.path.join(
                    food_folder, f"image_{image_counter}.jpg")

                # Write the image to a file
                with open(image_filename, 'wb') as img_file:
                    img_file.write(response.content)

                # Replace the URL in the DataFrame with the downloaded filename
                # Update the URL column
                df.at[index, 0] = f"image_{image_counter}.jpg"

                # Increment the global image counter
                image_counter += 1

            except requests.exceptions.RequestException as e:
                print(f"Error downloading {url}: {e}")

        # After processing the CSV, save the updated DataFrame back to the CSV file
        df.to_csv(os.path.join(csv_folder, csv_file),
                  header=False, index=False)

print("Image download completed and CSV files updated.")

import pandas as pd
import os


input_folder = "D:/Documents/4th year files/CSC173/filipino_food_calories/filipino-food-classifier/notebooks/data/filipino_food"
output_folder = ".\data pre-processing\cleaned_duplicate"


os.makedirs(output_folder, exist_ok=True)

# Loop through all CSV files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        # Full path to the current CSV file
        file_path = os.path.join(input_folder, filename)

        # Load the data and remove duplicates
        data = pd.read_csv(file_path)
        original_count = len(data)
        cleaned_data = data.drop_duplicates()
        cleaned_count = len(cleaned_data)

        # Save the cleaned data to the output folder
        cleaned_file_path = os.path.join(output_folder, filename)
        cleaned_data.to_csv(cleaned_file_path, index=False)

        print(
            f"{filename}: {original_count} entries -> {cleaned_count} entries after cleaning.")

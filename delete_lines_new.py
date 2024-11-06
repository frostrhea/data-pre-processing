import pandas as pd


def delete_rows_from_csv(file_path, rows_to_delete, output_path):
    data = pd.read_csv(file_path)

    # Convert 1-based `rows_to_delete` directly to match pandas row indices
    cleaned_data = data.drop(index=[row - 2 for row in rows_to_delete])

    # Save the cleaned DataFrame to a new CSV
    cleaned_data.to_csv(output_path, index=False)
    print(f"Cleaned CSV saved to {output_path}")


csv_file_path = './data pre-processing/cleaned_invalid_links/turon.csv'
rows_to_remove = [5, 7, 14, 17, 19, 29, 35, 40, 41, 44, 45, 46, 47, 50, 53, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 82, 84, 85, 91, 92, 94, 95, 97, 101, 102, 105, 106, 112, 113,
                  118, 122, 129, 132, 133, 134, 137, 139, 143, 145, 146, 147, 148, 150, 151, 154, 155, 156, 157, 158, 158, 160, 161, 164, 165, 167, 168, 169, 173, 174, 175, 176, 179, 180, 181, 184]

output_csv_path = './data pre-processing/cleaned_unrelated_pics/turon_cleaned.csv'
delete_rows_from_csv(csv_file_path, rows_to_remove, output_csv_path)

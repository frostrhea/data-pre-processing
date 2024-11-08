import os
import pandas as pd
import requests
from io import BytesIO
from PIL import Image
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt


csv_folder_path = "./data pre-processing/cleaned_invalid_links"
output_folder = "./view_images"


os.makedirs(output_folder, exist_ok=True)

# Loop through each CSV file in the folder
for csv_file in os.listdir(csv_folder_path):
    if csv_file.endswith(".csv"):
        file_path = os.path.join(csv_folder_path, csv_file)
        data = pd.read_csv(file_path)

        # Define the PDF output path based on the CSV file name
        pdf_path = os.path.join(
            output_folder, f"{os.path.splitext(csv_file)[0]}_images_all.pdf")

        # Define a unique log file for each CSV
        log_file_path = os.path.join(
            output_folder, f"{os.path.splitext(csv_file)[0]}_failed_urls_log.txt")

        # Save all images to the PDF
        with PdfPages(pdf_path) as pdf, open(log_file_path, "w") as log_file:
            images_per_row = 5
            total_images = len(data)

            # Process each image based on its row index in the CSV file
            for i in range(0, total_images, images_per_row * images_per_row):
                fig, axes = plt.subplots(
                    nrows=images_per_row, ncols=images_per_row, figsize=(15, 15))

                for j in range(images_per_row * images_per_row):
                    row_idx = i + j
                    if row_idx >= total_images:
                        axes[j // images_per_row, j %
                             images_per_row].axis("off")
                        continue

                    # Extract URL and row index
                    url = data.iloc[row_idx, 0]
                    csv_line_number = row_idx + 2  # +2 because rows start at 1 in CSV, and headers add 1

                    try:
                        response = requests.get(
                            url, timeout=10)  # Increased timeout
                        img = Image.open(BytesIO(response.content))

                        # Display image with CSV line number as label
                        ax = axes[j // images_per_row, j % images_per_row]
                        ax.imshow(img)
                        ax.set_title(f"Line {csv_line_number}", fontsize=8)
                        ax.axis("off")
                    except Exception as e:
                        # Log failed URL with CSV line number
                        log_file.write(
                            f"Failed to load image at line {csv_line_number} in CSV: {url}\n")
                        print(
                            f"Could not load image at line {csv_line_number} in file {csv_file}: {e}")

                pdf.savefig(fig)
                plt.close(fig)

        print(f"Images for '{csv_file}' saved to '{pdf_path}'")
        print(
            f"Log of missing images for '{csv_file}' saved to '{log_file_path}'")

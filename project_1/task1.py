import os
import zipfile

# Define the exact local asset name and target destination folder
zip_path = "edgeai-tinyml/project_one/human+activity+recognition+using+smartphones.zip"
extract_path = "UCI HAR Dataset"

# Only execute work if it hasn't been done yet
if not os.path.exists(extract_path):
    if os.path.exists(zip_path):
        print(f"Found {zip_path}. Unpacking local archive...")

        # Open and extract the outer container
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(".")

        # Handle inner archive nesting if packaged recursively
        inner_zip = "UCI HAR Dataset.zip"
        if os.path.exists(inner_zip):
            print("Extracting inner dataset package...")
            with zipfile.ZipFile(inner_zip, 'r') as inner_ref:
                inner_ref.extractall(".")
            os.remove(inner_zip)

        print("Task 1 Complete: Dataset successfully extracted and ready for ingestiong. Zero network friction.")
    else:
        print(f"Error: Could not find '{zip_path}' in this folder.")
        print("Please ensure the zip file is in your project directory.")
else:
    print("Dataset folder already exists. Zero wasted steps.")

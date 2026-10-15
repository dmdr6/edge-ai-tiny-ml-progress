import os
import zipfile

# Use exact downloaded file name
zip_path = "human+activity+recognition+using+smartphones.zip"
extract_path = "UCI HAR Dataset"

if not os.path.exists(extract_path):
    if os.path.exists(zip_path):
        print(f"Found {zip_path}. Unpacking local archive...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(".")
            
        # Handle inner zip files if packed as a nested archive
        inner_zip = "UCI HAR Dataset.zip"
        if os.path.exists(inner_zip):
            print("Extracting inner dataset package...")
            with zipfile.ZipFile(inner_zip, 'r') as inner_ref:
                inner_ref.extractall(".")
            os.remove(inner_zip)
            
        print("Task 1 Complete: Dataset successfully extracted and ready for ingestion. Zero network friction.")
    else:
        print(f"Error: Could not find '{zip_path}' in this folder.")
        print("Please ensure the zip file is in your project directory.")
else:
    print("Dataset folder already exists. Zero wasted steps.")

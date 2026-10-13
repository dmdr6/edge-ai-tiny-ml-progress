import os
import zipfile

zip_path = "uci_har.zip"
extract_path = "UCI HAR Dataset"

if os.path.exists(zip_path):
    print("Found local zip file. Unpacking locally...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(".")
    print("Dataset ready for ingestion. Zero network friction.")
else:
    print(f"Error: Could not find '{zip_path}' in this folder.")
    print("Please make sure you placed the downloaded zip file in your project directory.")

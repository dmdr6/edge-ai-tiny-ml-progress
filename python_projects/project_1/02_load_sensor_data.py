import pandas as pd

# 1. Define the file name from Task 1
filename = "sensor_data.csv"

# 2. Load the CSV file into a Pandas DataFrame
df = pd.read_csv(filename)

# 3. Display the first few rows to verify it loaded correctly
print("Dataset successfully loaded:")
print(df.head())

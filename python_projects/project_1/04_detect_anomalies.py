import pandas as pd

# Step 1: Load the sensor dataset
filename = "sensor_data.csv"
df = pd.read_csv(filename)

# Step 2: Detect missing (null) values in the dataset
missing_values = df.isnull().sum()
print("--- Missing Values Report ---")
print(missing_values)

# Step 3: Detect invalid records based on physical limits
# Let's assume valid room/environment temperatures must be between -10°C and 60°C
lower_limit = -10.0
upper_limit = 60.0

invalid_records = df[
    (df["Temperature"] < lower_limit) | (df["Temperature"] > upper_limit)
]

# Step 4: Output the results
print("\n--- Invalid Records Report ---")
if invalid_records.empty:
  print("Clean system: No invalid temperature readings detected.")
else:
  print("Warning: Invalid records found!")
  print(invalid_records)

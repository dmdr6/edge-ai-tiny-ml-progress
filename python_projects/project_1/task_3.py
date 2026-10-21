import pandas as pd

# 1. Load the sensor dataset
filename = "sensor_data.csv"
df = pd.read_csv(filename)

# 2. Isolate the temperature readings column
temperatures = df["Temperature"]

# 3. Calcualte the required statistical metrics
mean_val = temperatures.mean()
median_val = temperatures.median()
min_val = temperatures.min()
max_val = temperatures.max()
std_val = temperatures.std()

# 4. Output the results clearly
print("--- Sensor Data Statistical Analysis ---")
print(f"Mean (Average):     {mean_val:.2f}°C")
print(f"Median:             {mean_val:.2f}°C")
print(f"Minimum:            {min_val:.2f}°C")
print(f"Maximum:            {max_val:.2f}°C")
print(f"Standard Deviation: {std_val:.2f}°C")

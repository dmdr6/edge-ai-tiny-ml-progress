import csv
from datetime import datetime, timedelta

# 1. Define the output file name
filename = "sensor_data.csv"

# 2. Create simulated timestamps and temperature readings
start_time = datetime.now()
data = []

for i in range(10):
    # Add 1 minute for each step to create a timeline
    timestamp = start_time + timedelta(minutes=i)
    temperature = 22.5 + (i * 0.4)  # Create temperature readings
    data.append([timestamp.strftime("%Y-%m-%d %H:%M:%S"), temperature])

# 3. Write the data directly to a CSV file
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["Timestamps", "Temperature"])
    # Write all the data rows at once
    writer.writerows(data)

print(f"Dataset '{filename}' created successfully!")

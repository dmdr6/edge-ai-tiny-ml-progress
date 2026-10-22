import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Load the dataset
filename = "sensor_data.csv"
df = pd.read_csv(filename)

# Step 2: Convert the Timestamp column to actual datetime objects
df["Timestamps"] = pd.to_datetime(df["Timestamps"])

# Step 3: Initialize the plot window
plt.figure(figsize=(10, 5))

# Step 4: Plot timestamp vs temperature with markers and lines
plt.plot(
    df["Timestamps"],
    df["Temperature"],
    marker="o",
    color="tab:blue",
    linestyle="-",
    linewidth=2,
)

# Step 5: Format the chart with labels, title, and grid
plt.title("Sensor Temperature Over Time", fontsize=14, fontweight="bold")
plt.xlabel("Timestamps", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)

# Rotate timestamp labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Step 6: Render the chart
plt.show()

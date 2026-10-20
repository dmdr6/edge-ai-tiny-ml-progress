import os
import pandas as pd
import matplotlib.pyplot as plt

# Define dataset path and raw inertial signal paths for all 3 axes
dataset_path = "UCI HAR Dataset"
x_path = os.path.join(dataset_path, "train", "Inertial Signals", "total_acc_x_train.txt")
y_path = os.path.join(dataset_path, "train", "Inertial Signals", "total_acc_y_train.txt")
z_path = os.path.join(dataset_path, "train", "Inertial Signals", "total_acc_z_train.txt")

if os.path.exists(x_path):
    print("Loading 3-axis raw inertial accelerometer streams...")

    # Using raw string r'\s+' to avoid syntax warnings
    acc_x = pd.read_csv(x_path, sep=r'\s+', header=None)
    acc_y = pd.read_csv(y_path, sep=r'\s+', header=None)
    acc_z = pd.read_csv(z_path, sep=r'\s+', header=None)

    print(f"Succeed! Data matrix shape per axis: {acc_x.shape} (Windows × Time-steps)")

    # Select a dynamic motion window (i.e., index 500) to inspect active movement
    window_idx = 500
    signal_x = acc_x.iloc[window_idx]
    signal_y = acc_y.iloc[window_idx]
    signal_z = acc_z.iloc[window_idx]

    # Plot the 3-axis sensor wave
    plt.figure(figsize=(12, 6))
    plt.plot(signal_x, label='X-Axis (Lateral)', color='#ff7f0e', linewidth=1.2)
    plt.plot(signal_y, label='Y-Axis (Forward/Back)', color='#2ca02c', linewidth=1.2)
    plt.plot(signal_z, label='Z-Axis (Vertical)', color='#1f77b4', linewidth=1.2)

    plt.title(f"Task 2: Accelerometer Signals (Dynamic Window Index {window_idx})")
    plt.xlabel("Sample Index (Time-steps at 50 Hz)")
    plt.ylabel("Acceleration (g)")
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
else:
    print(f"Error: Could not locate inertial signal files in '{dataset_path}'.")
    print("Please verify that Task 1 unzipped the complete directory structure.")


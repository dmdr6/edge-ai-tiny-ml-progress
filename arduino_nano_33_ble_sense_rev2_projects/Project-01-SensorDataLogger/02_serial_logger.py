import serial

# Configure the serial connection (matching the port and baud rate)
port = "/dev/cu.usbmodem101"    # My board's active port
baud = 9600

ser = serial.Serial(port, baud, timeout=1)
print(f"Listening on {port}...")

with open("sensor_data_rev2.csv", "w") as f:
    try:
        while True:
            # Read a single line from the serial port and decode it from bytes to text
            line = ser.readline().decode("utf-8").strip()
            if line:
                print(line)             # Print to terminal to see it live
                f.write(line + "\n")    # Write it permanently into the CSV file
    except KeyboardInterrupt:
        print("Logging stopped. Data saved to sensor_data_rev2.csv.")
        ser.close()

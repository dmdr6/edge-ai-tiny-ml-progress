#include <Arduino_BMI270_BMM150.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);    // Wait for Serial Monitor to open

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while(1);     // Halt execution if the sensor fails
  }

  Serial.println("IMU initialized successfully!");
  Serial.print("Accelerometer sample rate: ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");
  Serial.print("Gyroscope sample rate: ");
  Serial.print(IMU.gyroscopeSampleRate());
  Serial.println(" Hz");  
}

void loop() {
  float ax, ay, az;   // Variables for acceleration (X, Y, Z)
  float gx, gy, gz;   // Variables for gyroscope rotation (X, Y, Z)

  // Step 2: Check if new physical data is ready to be read from hardware buffers
  if (IMU.accelerationAvailable() && IMU.gyroscopeAvailable()) {

    // Step 3: Pull the raw data into the variables
    IMU.readAcceleration(ax, ay, az);
    IMU.readGyroscope(gx, gy, gz);

    // Step 4: Print labels and values
    Serial.print("Accel: ");
    Serial.print(ax); Serial.print("\t");
    Serial.print(ay); Serial.print("\t");
    Serial.print(az); Serial.print("\t | Gyro: ");
    Serial.print(gx); Serial.print("\t");
    Serial.print(gy); Serial.print("\t");
    Serial.println(gz);
  }
}

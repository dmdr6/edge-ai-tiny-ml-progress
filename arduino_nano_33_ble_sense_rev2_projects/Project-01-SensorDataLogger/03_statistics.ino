#include <Arduino_BMI270_BMM150.h>

// Variables for tracking statistics (Min, Max, Mean)
int sampleCount = 0;
const int batchSize = 50; // Calculate stats every 50 samples

float minX = 1000, maxX = -1000, sumX = 0;
float minY = 1000, maxY = -1000, sumY = 0;
float minZ = 1000, maxZ = -1000, sumZ = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial); // Wait for Serial Monitor to open

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.println("IMU initialized successfully.");
  Serial.print("Accelerometer sample rate: ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");
  Serial.print("Gyroscope sample rate: ");
  Serial.print(IMU.gyroscopeSampleRate());
  Serial.println(" Hz");
  Serial.println("Format: ACC_X, ACC_Y, ACC_Z, GYRO_X, GYRO_Y, GYRO_Z");
}

void loop() {
  float ax, ay, az;
  float gx, gy, gz;

  // Check if both accelerometer and gyroscope data are available
  if (IMU.accelerationAvailable() && IMU.gyroscopeAvailable()) {
    IMU.readAcceleration(ax, ay, az);
    IMU.readGyroscope(gx, gy, gz);

    // 1. Stream raw data (captured by your Python script into CSV)
    Serial.print(ax); Serial.print(",");
    Serial.print(ay); Serial.print(",");
    Serial.print(az); Serial.print(",");
    Serial.print(gx); Serial.print(",");
    Serial.print(gy); Serial.print(",");
    Serial.println(gz);

    // 2. Track values for Min, Max, and Mean (using X, Y, Z acceleration)
    if (ax < minX) minX = ax;
    if (ax > maxX) maxX = ax;
    sumX += ax;

    if (ay < minY) minY = ay;
    if (ay > maxY) maxY = ay;
    sumY += ay;

    if (az < minZ) minZ = az;
    if (az > maxZ) maxZ = az;
    sumZ += az;

    sampleCount++;

    // 3. Print out statistics every batch of 50 samples
    if (sampleCount >= batchSize) {
      Serial.println("\n--- ACCEL STATS (Last 50 samples) ---");
      Serial.print("X Axis -> Min: "); Serial.print(minX); Serial.print(" | Max: "); Serial.print(maxX); Serial.print(" | Mean: "); Serial.println(sumX / sampleCount);
      Serial.print("Y Axis -> Min: "); Serial.print(minY); Serial.print(" | Max: "); Serial.print(maxY); Serial.print(" | Mean: "); Serial.println(sumY / sampleCount);
      Serial.print("Z Axis -> Min: "); Serial.print(minZ); Serial.print(" | Max: "); Serial.print(maxZ); Serial.print(" | Mean: "); Serial.println(sumZ / sampleCount);
      Serial.println("--------------------------------------\n");

      // Reset variables for the next batch
      sampleCount = 0;
      minX = 1000; maxX = -1000; sumX = 0;
      minY = 1000; maxY = -1000; sumY = 0;
      minZ = 1000; maxZ = -1000; sumZ = 0;
    }
  }
}

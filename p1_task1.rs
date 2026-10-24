fn store_readings() -> Vec<f64> {
    // Initializing a mutable vector to store floating-point temperature readings (Celsius)
    let mut readings: Vec<f64> = vec![21.5, 23.0, 22.4, 24.1, 22.8];

    // Returning the stored sensor data
    readings
}

fn main() {
    // Call the function to store and retrieve the readings
    let sensor_data = store_readings();

    // Output the stored readings to the console
    println!("Initial sensor readings stored: {:?}", sensor_data);
}

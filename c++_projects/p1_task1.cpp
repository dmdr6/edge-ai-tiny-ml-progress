#include <iostream>

double celsiusToFahrenheit(double CelsiusValue) {
    double scalingFactor = 1.8;
    double offset = 32.0;

    double fahrenheitValue = (CelsiusValue * scalingFactor) + offset;
    return fahrenheitValue;
}

int main() {
    // Test the function with a known value (e.g., the freezing point of water: 0°C)
    double testCelsius = 0.0;
    double result = celsiusToFahrenheit(testCelsius);

    // Output the result to the console
    std::cout << testCelsius << "°C is equal to " << result << "°F\n";

    return 0;
}

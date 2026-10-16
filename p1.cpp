#include <iostream>
#include <vector>

// Constants defining the physical limits of the simulated temperature sensor
const double ABSOLUTE_MIN = -50.0f;
const double ABSOLUTE_MAX = 150.0f;

int main() {
    std::vector<float> sensorReadings;
    float inputVal;
    char continueChoice = 'y';

    std::cout << "=== SENSOR DATA PIPELINE: PHASE 1 (VALIDATION & STORAGE) ===\n";
    std::cout << "Acceptable range: " << ABSOLUTE_MIN << " to " << ABSOLUTE_MAX << " units.\n\n";

    // Loop to stream/simulate incoming sensor data
    while(continueChoice == 'y' || continueChoice == 'Y') {
        std::cout << "Enter sensor reading: ";

        // Input validation for type safety
        if (!(std::cin >> inputVal)) {
            std::cout << "Error: Invalid data type entered. Exiting input loop.\n";
            break;
        }

        // First-Principles Constraint Check (Physics/Limits)


    }
}

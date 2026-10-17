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
    while(continueChoice == 'y' | continueChoice == 'Y') {
        std::cout << "Enter sensor reading: ";

        // Input validation for type safety
        if(!(std::cin >> inputVal)) {
            std::cout << "Error: Invalid data type entered. Exiting input loop.\n";
            break;
        }

        // First Principles Constraint Check (Physics/Limits)
        if (inputVal >= ABSOLUTE_MIN && inputVal <= ABSOLUTE_MAX) {
            sensorReadings.push_back(inputVal);
            std::cout << " [SUCCESS] Reading accepted and stored.\n";
        } else {
            std::cout << " [DROPPED] Out-of-bounds reading detected! Discarded for safety.\n";
        }

        std::cout << "Add another reading? (y/n): ";
        std::cin >> continueChoice;
    }

    // Summary of stored data
    std::cout << "\n--- Pipeline Status Update ---\n";
    std::cout << "Total valid readings stored: " << sensorReadings.size() << "\n";
    std::cout << "Stored values: ";
    for (float val : sensorReadings) {
        std::cout << val << " ";
    }
    std::cout << "\n";

    return 0;
}

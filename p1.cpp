#include <iostream>
#include <vector>

// Constants defining physical limits
const float ABSOLUTE_MIN = -50.0f;
const float ABSOLUTE_MAX = 150.0f;

// --- PHASE 2: STATISTICAL FUNCTIONS ---

// 1. Calculate Minimum
float calculateMin(const std::vector<float>& data) {
    if (data.empty()) return 0.0f;
    float minValue = data[0];
    for (float val : data) {
        if (val < minValue) {
            minValue = val;
        }
    }
    return minValue;
}

// 2. Calculate Maximum
float calculateMax(const std::vector<float>& data) {
    if (data.empty()) return 0.0f;
    float maxValue = data[0];
    for (float val : data) {
        if (val > maxValue) {
            maxValue = val;
        }
    }
    return maxValue;
}

// 3. Calculate Average
float calculateAverage(const std::vector<float>& data) {
    if (data.empty()) return 0.0f;
    float sum = 0.0f;
    for (float val : data) {
        sum += val;
    }
    return sum / data.size();
}

// 4. Calculate Range
float calculateRange(const std::vector<float>& data) {
    if (data.empty()) return 0.0f;
    return calculateMax(data) - calculateMin(data);
}

// --- MAIN PROGRAM ---
int main() {
    std::vector<float> sensorReadings;
    float inputVal;
    char continueChoice = 'y';

    std::cout << "=== SENSOR DATA PIPELINE: PHASES 1 & 2 ===\n";
    std::cout << "Acceptable range: " << ABSOLUTE_MIN << " to " << ABSOLUTE_MAX << " units.\n\n";

    // Phase 1: Input & Validation Loop
    while (continueChoice == 'y' || continueChoice == 'Y') {
        std::cout << "Enter sensor reading: ";
        
        if (!(std::cin >> inputVal)) {
            std::cout << "Error: Invalid data type entered. Exiting input loop.\n";
            break;
        }

        if (inputVal >= ABSOLUTE_MIN && inputVal <= ABSOLUTE_MAX) {
            sensorReadings.push_back(inputVal);
            std::cout << " [SUCCESS] Reading accepted.\n";
        } else {
            std::cout << " [DROPPED] Out-of-bounds reading discarded.\n";
        }

        std::cout << "Add another reading? (y/n): ";
        std::cin >> continueChoice;
    }

    // Check if we have data before computing stats
    if (sensorReadings.empty()) {
        std::cout << "\nNo valid sensor readings recorded. Exiting.\n";
        return 0;
    }

    // Phase 2: Compute and Display Analytical Report
    std::cout << "\n--- Sensor Measurement Analyzer Report ---\n";
    std::cout << "Total Valid Readings : " << sensorReadings.size() << "\n";
    std::cout << "Minimum Value        : " << calculateMin(sensorReadings) << "\n";
    std::cout << "Maximum Value        : " << calculateMax(sensorReadings) << "\n";
    std::cout << "Average Value        : " << calculateAverage(sensorReadings) << "\n";
    std::cout << "Sensor Range         : " << calculateRange(sensorReadings) << "\n";
    std::cout << "------------------------------------------\n";

    return 0;
}

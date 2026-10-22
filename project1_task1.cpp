#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int main() {
    vector<double> measurements;
    double inputVal;
    int numReadings;

    // Ask for the count of readings
    cout << "Enter the number of sensor readings you want to input: ";
    while (!(cin >> numReadings) || numReadings <= 0) {
        cout << "Invalid input. Please enter a positive integer: ";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    // Collect the sensor measurements
    cout << "Enter " << numReadings << " measurements (temperature or acceleration):\n";
    for (int i = 0; i < numReadings; ++i) {
        while(!(cin >> inputVal)) {
            cout << "Invalid measurement. Please enter a valid number: ";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        measurements.push_back(inputVal);
    }

    cout << "\nSuccessfully recorded " << measurements.size() << " measurements!\n";
    return 0;
}

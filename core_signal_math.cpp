#include <iostream>
#include <vector>
#include <cmath>
#include <cassert>

// Fundamental configuration structure
struct SignalConfig {
    double frequency = 440.0;    // Hz (standard A4 concert pitch)
    double amplitude = 1.0;      // Peak amplitude
};

// Electrical metrics structure
struct SignalMetrics {
    double peak = 0.0;
    double rms = 0.0;
};

// Pure mathematical evaluation for a single sample
class CoreSignalMath {
    public:
    // Sine wave calculations: y(t) = A * sin(2* pi * f * t)
    static double evaluateSine(double t, const SignalConfig& config) {
        return config.amplitude * std::sin(2.0 * M_PI * config.frequency * t);
    }
}

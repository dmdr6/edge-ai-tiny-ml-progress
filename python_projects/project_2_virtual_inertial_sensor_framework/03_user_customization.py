import numpy as np

def generate_base_signal(activity, duration=5, sampling_rate=50):
    """Generates pure mathematical baseline for each activity."""
    num_samples = int(duration * sampling_rate)         # Calculates total number of data points needed
    time = np.linspace(0, duration, num_samples)        # Creates an evenly spaced time array

    if activity == "stationary":
        # Flat baseline at zero
        signal = np.zeros(num_samples)
    elif activity == "walking":
        # Clean rhythmic wave
        signal = 1.5 * np.sin(2 * np.pi * 2 * time)
    elif activity == "shaking":
        # High-intensity chaotic baseline
        signal = np.random.uniform(-2.5, 2.5, num_samples)
    else:
        raise ValueError(
            "Invalid activity! Choose: 'stationary', 'walking', or 'shaking'"
        )

    return time, signal

def add_noise(signal, noise_level=0.1):
    """Injects realistic random sensor noise (Gaussian distribution)"""
    # Generate random noise matching the length of the signal
    noise = np.random.normal(loc=0.0, scale=noise_level, size=len(signal))

    # Superimpose noise onto the clean signal
    noisy_signal = signal + noise
    return noisy_signal


def main():
    """Interactive command-line interface for user customization."""
    print("=== Virtual Inertial Sensor Framework (VISF) ===")
    print("Available activities: stationary, walking, shaking\n")

    # Get user input
    activity = input(
        "Enter activity (stationary/walking/shaking): "
    ).strip().lower()
    duration = float(input("Enter duration in seconds (e.g., 5): "))
    sampling_rate = int(input("Enter sampling rate in Hz (e.g., 50): "))
    noise_level = float(input("Enter noise level intensity (e.g., 0.1): "))

    # Execute generation
    try:
        time, base_signal = generate_base_signal(
            activity, duration, sampling_rate
        )
        final_signal = add_noise(base_signal, noise_level)

        print("\n[SUCCESS] Signal generated successfully!")
        print(f"Total samples: {len(final_signal)}")
        print(f"Time span: {duration} seconds at {sampling_rate} Hz")

    except ValueError as e:
        print(f"\n[ERROR] {e}")


if __name__ == "__main__":
    main()

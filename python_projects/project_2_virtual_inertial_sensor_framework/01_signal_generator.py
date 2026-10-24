import numpy as np

def generate_signal(activity, duration=5, sampling_rate=50):
    """ Generates synthetic sensor signals for stationary, walking, and shaking.

    - duration: length of recording in seconds
    - sampling rate: samples per second (Hz)
    """
    # Calculate total number of data points needed
    num_samples = duration * sampling_rate

    # Create an evenly spaced time array
    time = np.linspace(0, duration, num_samples)

    # Generate activity-specific signal patterns
    if activity == "stationary":
        # Flat baseline close to zero with minuscule sensor noise
        signal = np.zeros(num_samples) + np.random.normal(0, 0.02, num_samples)
   
    elif activity == "walking":
        # Rhythmic sine wave (approx. 2 steps per second) plus organic body variance
        signal = 1.5 * np.sin(2 * np.pi * 2 * time) + np.random.normal(
            0, 0.15, num_samples
        )
   
    elif activity == "shaking":
        # High-intensity, high-frequency random chaos
        signal = np.random.normal(0, 3.0, num_samples)
   
    else:
        raise ValueError(
            "Invalid activity! Choose: 'stationary', 'walking', 'shaking'"
        )

    return time, signal

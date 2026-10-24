import numpy as np

def generate_base_signal(activity, duration=5, sampling_rate=50):
    """Generates the pure mathematical baseline for each activity."""
    num_samples = duration * sampling_rate
    time = np.linspace(0, duration, num_samples)

    if activity == "stationary":
        # Perfect flatline at zero
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
    """ Injects realistic random sensor noise (Gaussian distribution).
    
    - noise_level: Controls the intensity/amplitude of the noise.
    """
    # Generate random noise matching the length of the signal
    noise = np.random.normal(loc=0.0, scale=noise_level, size=len(signal))

    # Superimpose noise onto the clean signal
    noisy_signal = noise + signal
    return noisy_signal


import numpy as np
import matplotlib.pyplot as plt

def generate_signal(signal_type, frequency, amplitude, duration, sample_rate):
    """
    First-principles signal generator using NumPy vectorization.
    Deletes object-oriented bloat in favor of direct mathematical mapping.
    """
    # Time vector: discrete points from 0 to duration
    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)

    if signal_type == "sine":
        signal = amplitude * np.sin(2 * np.pi * frequency * t)
    elif signal_type == "square":
        signal = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))
    elif signal_type == "noise":
        signal = amplitude * np.random.uniform(-1, 1, size=t.shape)
    else:
        raise ValueError(f"Unknown signal type: {signal_type}")

    return t, signal

def calculate_stats(signal):
    """Calculate RMS and peak amplitude directly from the discrete array."""
    rms = np.sqrt(np.mean(signal**2))
    peak_amp = np.max(np.abs(signal))
    return rms, peak_amp

# --- Quick Test Execution ---
fs = 1000   # Sample rate (Hz)
t, sine_wave = generate_signal("sine", frequency=5, amplitude=2.0, duration=1.0, sample_rate=fs)
rms, peak_amp = calculate_stats(sine_wave)

print(f"Sine Wave Stats -> Peak Amplitude: {peak_amp:.2f} | RMS: {rms:.2f}")

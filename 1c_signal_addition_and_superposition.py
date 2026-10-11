import numpy as np
import matplotlib.pyplot as plt

def generate_signal(signal_type, frequency, amplitude, duration, sample_rate):
    """Reusable signal generator from Phase 1A."""
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

def run_addition_experiment():
    fs = 1000  # 1000 Hz sample rate
    duration = 1.0
    
    # 1. Generate two distinct signals
    t, sig1 = generate_signal("sine", frequency=5.0, amplitude=1.0, duration=duration, sample_rate=fs)
    _, sig2 = generate_signal("sine", frequency=50.0, amplitude=0.3, duration=duration, sample_rate=fs)
    
    # 2. Superposition (Signal Addition) - just pure vector math!
    combined_signal = sig1 + sig2
    
    # 3. Automate multi-plot layout
    plt.figure(figsize=(10, 6))
    
    plt.subplot(3, 1, 1)
    plt.plot(t, sig1, color='blue')
    plt.title("Signal 1: Base Tone (5 Hz)")
    plt.grid(True)
    
    plt.subplot(3, 1, 2)
    plt.plot(t, sig2, color='green')
    plt.title("Signal 2: High Frequency Component (50 Hz)")
    plt.grid(True)
    
    plt.subplot(3, 1, 3)
    plt.plot(t, combined_signal, color='purple')
    plt.title("Superposition (Signal 1 + Signal 2)")
    plt.xlabel("Time (s)")
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Run the superposition test
run_addition_experiment()

import numpy as np
import matplotlib.pyplot as plt

def plot_aliasing_experiment():
    # 1. Define a high-frequency signal (e.g., 11 Hz)
    f_signal = 11.0
    duration = 1.0
    amplitude = 1.0

    # High-resolution time vector to simulate "continuous" analog reality
    t_continuous = np.linspace(0, duration, 2000, endpoint=False)
    y_continuous = amplitude * np.sin(2 * np.pi * f_signal * t_continuous)

    # 2. Undersample the signal (e.g., sample rate of 15 Hz -> violates Nyquist 2f rule)
    fs = 15.0
    t_sampled = np.linspace(0, duration, int(duration * fs), endpoint=False)
    y_sampled = amplitude * np.sin(2 * np.pi * f_signal * t_sampled)

    # 3. Plot the deception (Automate step)
    plt.figure(figsize=(10, 4))

    plt.plot(
        t_continuous,
        y_continuous,
        label=f"True Signal ({f_signal} Hz)",
        color="gray",
        alpha=0.6
    )

    plt.stem(
        t_sampled,
        y_sampled,
        linefmt="r-",
        markerfmt="ro",
        basefmt="k-",
        label=f"Sampled Points (fs = {fs} Hz)"
    )

    plt.title("The Aliasing Phenomenon: Undersampling a Sine Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the experiment
plot_aliasing_experiment()

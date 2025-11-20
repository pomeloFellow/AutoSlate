# helper funcs
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import random


def log(message):
    """Writes to terminal in format [LOG]<text>

    Args:
        message (string): Message to log
    """
    print(f"[LOG] {message}")

def log_function_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"The function '{func.__name__}' returned: {result}")
        return result
    return wrapper

def plot_waveform_with_peaks(audio, threshold=0.99, sample_rate=16000):
    """
    Plots audio waveform with clipping/peak markers, x-axis in seconds,
    and saves to a file in test/waveforms with a random filename.
    """
    # Find peaks above threshold
    peaks = np.where(np.abs(audio) >= threshold)[0]

    # Time axis in seconds
    t = np.arange(len(audio)) / sample_rate

    # Create figure
    plt.figure(figsize=(12, 5))
    plt.plot(t, audio, label="Waveform", alpha=0.7)
    plt.scatter(t[peaks], audio[peaks], color="red", s=10, label="Clipping / near-clipping")

    # Reference lines for ±threshold
    plt.axhline(threshold, color="orange", linestyle="--", linewidth=1)
    plt.axhline(-threshold, color="orange", linestyle="--", linewidth=1)

    plt.title("Audio waveform with clipping detection")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.tight_layout()

    # Ensure output directory exists
    output_dir = Path("test/waveforms").expanduser().resolve(strict=False)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate random filename and save
    output_path = output_dir / f"waveform_{random.randint(1, 1000)}.png"
    plt.savefig(output_path, dpi=300)
    plt.close()  # Close figure to free memory




import numpy as np
import matplotlib.pyplot as plt
import csv

from signal_metrics import calculate_peak_amplitude, calculate_rms_amplitude, calculate_peak_dbfs



frequency = float(input("Enter frequency in Hz: "))
sample_rate = int(input("Enter sample rate in Hz: "))
duration = float(input("Enter duration in seconds: "))
amplitude = float(input("Enter amplitude (0 to 1): "))


if frequency <= 0:
    raise ValueError("Frequency must be greater than zero.")

if sample_rate <= 0:
    raise ValueError("Sample rate must be greater than zero.")

if duration <= 0:
    raise ValueError("Duration must be greater than zero.")

if not 0 <= amplitude <= 1:
    raise ValueError("Amplitude must be between 0 and 1.")

if frequency >= sample_rate / 2:
    raise ValueError("Frequency must be below the Nyquist frequency.")




number_of_samples = int(duration * sample_rate)
time = np.arange(number_of_samples) / sample_rate
signal = amplitude * np.sin(2 * np.pi * frequency * time) 

peak_amplitude = calculate_peak_amplitude(signal)
rms_amplitude = calculate_rms_amplitude(signal)
peak_dbfs = calculate_peak_dbfs(peak_amplitude)

print("\n ____Audio Signal Analysis____")
print(f"Frequency: {frequency} Hz")
print(f"Sample Rate: {sample_rate} Hz")
print(f"number of Samples: {number_of_samples}")
print(f"First 5 samples of the signal: {signal[:5]}")
print(f"Peak Amplitude: {peak_amplitude:.4f}")
print(f"RMS Amplitude: {rms_amplitude:.4f}")
print(f"Peak Amplitude in dBFS: {peak_dbfs:.2f} dBFS")

number_of_visible_samples = int(sample_rate * 0.005)

plt.plot(
    time[:number_of_visible_samples],
    signal[:number_of_visible_samples]
)
plt.title("First 5 ms Of Generated Audio Signal")
plt.xlabel("time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()


with open("audio_measurements.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Frequency (Hz)",
        "Sample Rate (Hz)",
        "Duration (seconds)",
        "Peak Amplitude",
        "RMS Amplitude",
        "Peak Amplitude (dBFS)"
    ])

    writer.writerow([
        frequency,
        sample_rate,
        duration,
        peak_amplitude,
        rms_amplitude,
        peak_dbfs
    ])

print("Measurements saved to audio_measurements.csv")


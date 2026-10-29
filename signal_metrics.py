import numpy as np

def calculate_peak_amplitude(signal):
    return np.max(np.abs(signal))

def calculate_rms_amplitude(signal):
    return np.sqrt(np.mean(signal**2))

def calculate_peak_dbfs(peak_amplitude):
    if peak_amplitude > 0:
        return 20 * np.log10(peak_amplitude)
    else:
        return float("-inf")
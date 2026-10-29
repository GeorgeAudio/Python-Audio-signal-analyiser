import unittest 
import numpy as np

from signal_metrics import(
    calculate_peak_amplitude,
    calculate_rms_amplitude,
    calculate_peak_dbfs
)

class TestSignalMetrics(unittest.TestCase):

    def test_calculate_peak_amplitude(self):
        signal = np.array([-0.5, 0.2, 1.0, -0.1])
        self.assertAlmostEqual(calculate_peak_amplitude(signal), 1.0)

    def test_calculate_rms_amplitude(self):
        signal = np.array([3.0, 4.0])
        expected_rms = np.sqrt((3.0**2 + 4.0**2) / 2)
        self.assertAlmostEqual(calculate_rms_amplitude(signal), expected_rms)

    def test_zero_dbfs(self):
        self.assertAlmostEqual(calculate_peak_dbfs(1.0), 0.0)

    def test_half_amplitude_dbfs(self):
        result = calculate_peak_dbfs(0.5)
        self.assertAlmostEqual(result, -6.0206, places=3)

    def test_silence_dbfs(self):
        result = calculate_peak_dbfs(0.0)
        self.assertEqual(result, float("-inf"))


if __name__ == "__main__":
    unittest.main()


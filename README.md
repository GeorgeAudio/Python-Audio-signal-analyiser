# Python Audio Signal Analyser

## About the project

I built this project to improve my Python skills and learn more about digital signal processing. I wanted to understand how audio signals can be generated digitally and how different measurements can be used to analyse them.

The program generates a sine wave based on the settings entered by the user, calculates measurements from the signal, displays a graph of the waveform and saves the results to a CSV file.

## What it does

- Generates sine waves with adjustable frequency, amplitude, sample rate and duration.
- Calculates peak amplitude and RMS amplitude.
- Converts peak amplitude into dBFS.
- Displays the waveform using Matplotlib.
- Exports measurements to a CSV file.
- Checks user inputs to help prevent invalid signal settings.
- Includes automated tests to check that the calculations give the expected results.

## Tools used

- Python
- NumPy
- Matplotlib
- CSV
- unittest

## How it works

The program uses a sine wave equation to generate digital audio samples. These samples are then used to calculate the signal measurements.

I used NumPy to handle the calculations and Matplotlib to plot the waveform. I also separated the measurement functions into their own Python file so that I could test them independently.

One of the things I learned was how RMS amplitude differs from peak amplitude. For example, a sine wave with a peak amplitude of 1 has an RMS amplitude of approximately 0.707.

## How to run it

First, install the required Python libraries:


python3 -m pip install numpy matplotlib

Run the program using:


python3 audio_analyser.py


Enter the signal settings when prompted. The program will calculate the measurements, display the waveform and save the results to a CSV file.

## Testing

I created unit tests to check that the measurement functions produce the expected results.

To run the tests:


python3 -m unittest -v test_signal_metrics.py


The tests cover peak amplitude, RMS amplitude, dBFS calculations and how the program handles a signal with zero amplitude.

## What I've learned

Through this project, I've gained practical experience with Python, NumPy, digital signal generation, amplitude measurements, plotting data and writing automated tests. It has also helped me understand how mathematical concepts can be applied to audio engineering.

## Future improvements

I'd like to develop the project further by adding the ability to analyse real WAV files, measure frequency response and eventually compare signals recorded from physical audio equipment.


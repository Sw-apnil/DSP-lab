# WAP to design a 25 tap low pass FIR filter with cutoff = 0.5*pi radians
# using 1. Rectangular window 2. Hamming window and plot frequency response

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Filter parameters
N = 25  # Number of taps

# Cutoff frequency (given in radians/sample)
wc = 0.5 * np.pi

# Convert to normalized frequency (firwin needs 0 to 0.5)
fc = wc / (2 * np.pi)   # = 0.25

# FIR filter design
h_rect = signal.firwin(N, fc, window='boxcar')   # Rectangular window
h_hamming = signal.firwin(N, fc, window='hamming')  # Hamming window

# Frequency response
w, H_rect = signal.freqz(h_rect, worN=8000)
w, H_hamming = signal.freqz(h_hamming, worN=8000)

# Plot
plt.figure(figsize=(10,6))

plt.plot(w, np.abs(H_rect), label='Rectangular Window')
plt.plot(w, np.abs(H_hamming), label='Hamming Window')

# Mark cutoff frequency at 0.5*pi
plt.axvline(x=0.5*np.pi, color='red', linestyle='--', label='Cutoff (0.5π)')

# Labels and styling
plt.title('Frequency Response of 25-Tap FIR Low Pass Filter')
plt.xlabel('Frequency (radians/sample)')
plt.ylabel('Magnitude')
plt.legend()
plt.grid()

plt.show()
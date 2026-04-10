#WAP to overlap  save algorithm for filtering of long data sequence. (language: python)

import numpy as np
import matplotlib.pyplot as plt

# Input signal
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Impulse response
h = np.array([1, -1, 2])

# Lengths
M = len(h)
L = 4                     # block size
N = L + M - 1             # FFT size

# FFT of filter
H = np.fft.fft(h, N)

# Output
y = np.zeros(len(x) + M - 1)

# 🔥 Overlap-Add Implementation
i = 0
while i < len(x):
    # Step 1: Take block
    block = x[i:i+L]

    # Step 2: Pad block to length L (important!)
    if len(block) < L:
        block = np.pad(block, (0, L - len(block)))

    # Step 3: Pad to N
    block_padded = np.pad(block, (0, N - L))

    # Step 4: FFT → Multiply → IFFT
    X = np.fft.fft(block_padded)
    Y = X * H
    y_block = np.real(np.fft.ifft(Y))

    # Step 5: Add safely (no overflow)
    for k in range(N):
        if (i + k) < len(y):
            y[i + k] += y_block[k]

    i += L

# ✅ Reference (True Linear Convolution)
y_linear = np.convolve(x, h)

# PRINT
print("Overlap-Add Output:      ", y)
print("Linear Convolution Output:", y_linear)

# VERIFY
if np.allclose(y, y_linear):
    print("✅ Outputs MATCH perfectly!")
else:
    print("❌ Outputs DO NOT match!")

# PLOT
plt.figure()

plt.subplot(3,1,1)
plt.stem(x)
plt.title("Input Signal")

plt.subplot(3,1,2)
plt.stem(y)
plt.title("Overlap-Add Output")

plt.subplot(3,1,3)
plt.stem(y_linear)
plt.title("Linear Convolution Output")

plt.tight_layout()
plt.show()
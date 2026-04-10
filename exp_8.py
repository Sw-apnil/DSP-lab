#WAP to overlap add algorithm for filtering of long data sequence. (language: python)
import numpy as np
import matplotlib.pyplot as plt

# Input signal
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Filter
h = np.array([1, -1, 2])

M = len(h)
L = 4
N = L + M - 1

H = np.fft.fft(h, N)

y = np.zeros(len(x) + M - 1)

# ✅ Overlap-Add (FINAL FIXED)
for i in range(0, len(x), L):
    block = x[i:i+L]

    # Step 1: make block length L
    if len(block) < L:
        block = np.pad(block, (0, L - len(block)))

    # Step 2: pad to N
    block_padded = np.pad(block, (0, N - L))

    X = np.fft.fft(block_padded)
    Y = X * H
    y_block = np.fft.ifft(Y)

    # ✅ Step 3: SAFE ADD (important)
    end = min(i + N, len(y))
    y[i:end] += np.real(y_block[:end - i])

# ✅ Linear convolution (reference)
y_linear = np.convolve(x, h)

print("Overlap-Add Output:      ", y)
print("Linear Convolution Output:", y_linear)

# Plot
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
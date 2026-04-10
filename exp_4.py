#WAP to  find out circular convolution of two  sequences having different length. use the logic of circular  convolution
#and check the result with the inbuilt circular convolution. (language: python)

import numpy as np

# Input sequences
x = [1, 2, 3]
h = [4, 5]

# Step 1: Make same length
N = max(len(x), len(h))

x = x + [0] * (N - len(x))
h = h + [0] * (N - len(h))

# Step 2: Circular Convolution (manual)
y = [0] * N

for n in range(N):
    for k in range(N):
        y[n] += x[k] * h[(n - k) % N]

print("Manual Circular Convolution:", y)


# Inbuilt using FFT
X = np.fft.fft(x)
H = np.fft.fft(h)

Y = X * H

y_fft = np.fft.ifft(Y)

print("Using FFT:", np.real(y_fft))
#WAP  to compute radix 2 -DITFFT of a sequence having length N=8.compare the output with the inbuilt FFT function. (language: python)


import numpy as np

def fft_dit(x):
    N = len(x)
    
    # Base case
    if N == 1:
        return x
    
    # Split into even and odd
    even = fft_dit(x[0::2])
    odd = fft_dit(x[1::2])
    
    X = [0] * N
    
    for k in range(N // 2):
        W = np.exp(-2j * np.pi * k / N)
        
        X[k] = even[k] + W * odd[k]
        X[k + N//2] = even[k] - W * odd[k]
    
    return X


# Input sequence (length must be 8)
x = [1, 2, 3, 4, 5, 6, 7, 8]

# Manual FFT
X_manual = fft_dit(x)

print("DIT-FFT Output:")
print(np.round(X_manual, 2))


# Inbuilt FFT
X_builtin = np.fft.fft(x)

print("\nBuilt-in FFT Output:")
print(np.round(X_builtin, 2))
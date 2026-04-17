
import numpy as np
import matplotlib.pyplot as plt

# Define range
n = np.arange(-5, 15)

# Unit step
def u(n):
    return np.where(n >= 0, 1, 0)

# Impulse response h(n)
h = (0.5)**n * u(n) - (0.5)**(n-3) * u(n-3)

# Input x(n)
x = 2*(n==0) + (n==1) - (n==3) - (n==-2)

# -----------------------------
# Manual Convolution using formula
# y(n) = 2h(n) + h(n-1) - h(n-3) - h(n+2)

h_n     = (0.5)**n * u(n) - (0.5)**(n-3) * u(n-3)
h_n1    = (0.5)**(n-1) * u(n-1) - (0.5)**(n-4) * u(n-4)
h_n3    = (0.5)**(n-3) * u(n-3) - (0.5)**(n-6) * u(n-6)
h_np2   = (0.5)**(n+2) * u(n+2) - (0.5)**(n-1) * u(n-1)

y_manual = 2*h_n + h_n1 - h_n3 - h_np2

# -----------------------------
# Inbuilt convolution
y_builtin = np.convolve(x, h)

# Proper index for builtin output
n_builtin = np.arange(n[0] + n[0], n[0] + n[0] + len(y_builtin))

# -----------------------------

plt.figure(figsize=(8,9))

# Input Signal
plt.subplot(3,1,1)
plt.stem(n, x)
plt.title("Input Signal x(n)")
plt.xlabel("n")
plt.ylabel("Amplitude")

# Manual Convolution Output
plt.subplot(3,1,2)
plt.stem(n, y_manual)
plt.title("Manual Convolution Output")
plt.xlabel("n")
plt.ylabel("Amplitude")

# Inbuilt Convolution Output
plt.subplot(3,1,3)
plt.stem(n_builtin, y_builtin)
plt.title("Inbuilt Convolution Output")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()


print("Manual Convolution Output:\n", y_manual)
print("Inbuilt Convolution Output:\n", y_builtin)
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# HELPER FUNCTION: Unit Step u(n)
# ==========================================
def u(n):
    """
    Returns 1 if n >= 0, else 0.
    """
    return np.where(n >= 0, 1.0, 0.0)

# ==========================================
# PART 1: Generate and Plot Elementary Signals
# ==========================================
def problem_1():
    # Define time range n from -5 to 10
    n = np.arange(-5, 11)

    # 1. Unit Impulse (Delta) d(n) -> 1 at n=0, else 0
    delta_n = np.where(n == 0, 1.0, 0.0)

    # 2. Unit Step u(n) -> 1 for n>=0
    u_n = u(n)

    # 3. Unit Ramp r(n) -> n for n>=0
    r_n = np.where(n >= 0, n, 0.0)

    # 4. Sinusoidal Signal -> sin(w*n)
    # Let's pick an arbitrary frequency, e.g., w = 0.2*pi
    x_sin = np.sin(0.2 * np.pi * n)

    # --- PLOTTING ---
    plt.figure(figsize=(10, 8))
    plt.suptitle('Problem 1: Elementary Signals', fontsize=16)

    # Plot Impulse
    plt.subplot(2, 2, 1)
    plt.stem(n, delta_n, basefmt=" ")
    plt.title(r'Unit Impulse $\delta[n]$')
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Plot Unit Step
    plt.subplot(2, 2, 2)
    plt.stem(n, u_n, basefmt=" ")
    plt.title('Unit Step $u[n]$')
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Plot Ramp
    plt.subplot(2, 2, 3)
    plt.stem(n, r_n, basefmt=" ")
    plt.title('Unit Ramp $r[n]$')
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Plot Sinusoidal
    plt.subplot(2, 2, 4)
    plt.stem(n, x_sin, basefmt=" ")
    plt.title(r'Sinusoidal $\sin(0.2\pi n)$')
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# ==========================================
# PART 2: Operations on Signal x(n)
# ==========================================
def problem_2():
    # Define a wider range for n to see shifts clearly
    n = np.arange(-15, 15)
    
    # 2a. Generate x(n)
    # Equation from board: x(n) = 2u(n) + 3u(n-4) - 5u(n-7)
    x_n = 2*u(n) + 3*u(n-4) - 5*u(n-7)

    # Define shift amount k (Let's assume k=3 for the demo)
    k = 3

    # 2b. Shift by k, then Flip
    # Mathematical derivation:
    # 1. Shift x(n) by k --> x(n-k)  (Delay)
    # 2. Flip the result --> x(-n-k) (Replace n with -n)
    y_b = 2*u(-n-k) + 3*u(-n-k-4) - 5*u(-n-k-7)

    # 2c. Flip first, then Shift by k
    # Mathematical derivation:
    # 1. Flip x(n) --> x(-n)
    # 2. Shift the result by k --> x(-(n-k)) = x(-n+k)
    y_c = 2*u(-n+k) + 3*u(-n+k-4) - 5*u(-n+k-7)

    # --- PLOTTING ---
    plt.figure(figsize=(10, 10))
    plt.suptitle(f'Problem 2: Signal Operations (Shift k={k})', fontsize=16)

    # Original Signal
    plt.subplot(3, 1, 1)
    plt.stem(n, x_n, basefmt=" ", linefmt='b-', markerfmt='bo')
    plt.title(r'(a) Original Signal $x[n] = 2u[n] + 3u[n-4] - 5u[n-7]$')
    plt.grid(True)
    plt.ylabel('Amplitude')

    # Shift then Flip
    plt.subplot(3, 1, 2)
    plt.stem(n, y_b, basefmt=" ", linefmt='g-', markerfmt='go')
    plt.title(r'(b) Shift then Flip: Result is $x[-n-k]$ (Moves Left)')
    plt.grid(True)
    plt.ylabel('Amplitude')

    # Flip then Shift
    plt.subplot(3, 1, 3)
    plt.stem(n, y_c, basefmt=" ", linefmt='r-', markerfmt='ro')
    plt.title(r'(c) Flip then Shift: Result is $x[-n+k]$ (Moves Right)')
    plt.grid(True)
    plt.xlabel('Sample (n)')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()

# Run the functions
if __name__ == "__main__":
    problem_1()
    problem_2()
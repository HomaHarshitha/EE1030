import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./libsect.so')

# Define the function prototype
lib.main.argtypes = []  # No arguments for main
lib.main.restype = ctypes.c_int  # Return type is int

def call_c_code():
    result = lib.main()  # Call the main function from C
    return result

def plot_points():
    # Coordinates of points A, B, and P
    A = np.array([2, 3])
    B = np.array([6, -3])
    P = np.array([4, 0])  # Placeholder for y-coordinate

    # Call the C function to get the value of m
    call_c_code()  # This updates the y-coordinate of P

    # Plot the points and the line segment
    plt.figure(figsize=(10, 10))
    plt.plot([A[0], B[0]], [A[1], B[1]], 'ro-', label='Line AB')  # Line segment AB
    plt.plot(A[0], A[1], 'bo', label='Point A (2, 3)')
    plt.plot(B[0], B[1], 'go', label='Point B (6, -3)')
    plt.plot(P[0], P[1], 'mo', label=f'Point P (4, {P[1]})')  # P with calculated y-coordinate
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.title('Plot of Points A, B, and P')
    plt.show()

if __name__ == '__main__':
    plot_points()


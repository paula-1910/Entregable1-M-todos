import numpy as np

# Define the target function f(x) = e^x * sin(x)
def f(x):
    return np.exp(x) * np.sin(x)

# Problem parameters: evaluation point x0 = 0.5 and step size h = 0.1
x0 = 0.5
h = 0.1

# -------------------------------------------------------------
# Part (B): Centered Finite Difference Approximation
# -------------------------------------------------------------
# Evaluate function values at the required 4 stencil points:
# x_0 + 2h, x_0 + h, x_0 - h, x_0 - 2h
f_p2 = f(x0 + 2*h)  # f(0.7)
f_p1 = f(x0 + h)    # f(0.6)
f_m1 = f(x0 - h)    # f(0.4)
f_m2 = f(x0 - 2*h)  # f(0.3)

# Centered difference formula numerator: f(x_0+2h) - 2f(x_0+h) + 2f(x_0-h) - f(x_0-2h)
numerator = f_p2 - 2*f_p1 + 2*f_m1 - f_m2

# Denominator: 2 * h^3
denominator = 2 * (h**3)

# Compute the numerical approximation for f'''(0.5)
f3_numerical = numerator / denominator

# -------------------------------------------------------------
# Part (C): Exact Analytical Derivative and Error Calculation
# -------------------------------------------------------------
# Exact third derivative: f'''(x) = 2 * e^x * (cos(x) - sin(x))
f3_exact = 2 * np.exp(x0) * (np.cos(x0) - np.sin(x0))

# Compute absolute error: |Exact - Numerical|
absolute_error = abs(f3_exact - f3_numerical)

# Compute relative error: Absolute Error / |Exact|
relative_error = absolute_error / abs(f3_exact)

# Display all formatted results
print(f"f(0.7) = {f_p2:.6f}")
print(f"f(0.6) = {f_p1:.6f}")
print(f"f(0.4) = {f_m1:.6f}")
print(f"f(0.3) = {f_m2:.6f}")
print("-" * 40)
print(f"Numerical f'''(0.5): {f3_numerical:.6f}")
print(f"Exact f'''(0.5):     {f3_exact:.6f}")
print(f"Absolute Error:      {absolute_error:.6f}")
print(f"Relative Error:      {relative_error * 100:.3f}%")
import numpy as np
import matplotlib.pyplot as plt

# Define the integrand function f(x) = exp(-x^2)
f = lambda x: np.exp(-x**2)

# Define integration interval [a, b] and number of subintervals (n = 4)
a, b = 0, 2
n = 4
h = (b - a) / n  # Calculate the step size (h = 0.5)

# Generate the n+1 discrete integration nodes and evaluate f(x) at these nodes
x_nodes = np.linspace(a, b, n + 1)
y_nodes = f(x_nodes)

# Generate a fine grid of 400 points to plot the continuous target function smoothly
x_dense = np.linspace(a, b, 400)
y_dense = f(x_dense)

# Create a figure with 2 subplots side by side
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# --- i. Composite Trapezoidal Rule Plot ---
# Plot the exact continuous curve of f(x)
axes[0].plot(x_dense, y_dense, 'b-', label=r'$f(x) = e^{-x^2}$', lw=2)

# Loop through each subinterval to construct and shade the linear trapezoids
for i in range(n):
    # Coordinates defining the 4 vertices of each trapezoid
    xs = [x_nodes[i], x_nodes[i], x_nodes[i+1], x_nodes[i+1]]
    ys = [0, y_nodes[i], y_nodes[i+1], 0]
    
    # Fill the region under the trapezoid with a semi-transparent red color
    axes[0].fill(xs, ys, edgecolor='red', facecolor='red', alpha=0.2)
    
    # Draw the straight line segment connecting (x_i, y_i) to (x_{i+1}, y_{i+1})
    axes[0].plot([x_nodes[i], x_nodes[i+1]], [y_nodes[i], y_nodes[i+1]], 'r--', lw=1.5)

# Mark the discrete evaluation nodes with red circles
axes[0].plot(x_nodes, y_nodes, 'ro', label='Integration Nodes')
axes[0].set_title('Composite Trapezoidal Rule (n=4)')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].grid(True)
axes[0].legend()

# --- ii. Composite Simpson's 1/3 Rule Plot ---
# Plot the exact continuous curve of f(x)
axes[1].plot(x_dense, y_dense, 'b-', label=r'$f(x) = e^{-x^2}$', lw=2)

# Simpson's rule connects pairs of subintervals (3 consecutive nodes) using a quadratic parabola
for i in range(0, n, 2):
    # Extract 3 consecutive nodes: x_i, x_{i+1}, x_{i+2}
    x_sub = x_nodes[i:i+3]
    y_sub = y_nodes[i:i+3]
    
    # Fit a second-degree polynomial (parabola) through these 3 points
    poly = np.polyfit(x_sub, y_sub, 2)
    
    # Generate points across the pair of subintervals to plot the parabolic arc
    x_p = np.linspace(x_sub[0], x_sub[2], 100)
    y_p = np.polyval(poly, x_p)
    
    # Fill the region under the parabolic approximation with green shading
    axes[1].fill_between(x_p, 0, y_p, edgecolor='green', facecolor='green', alpha=0.2)
    
    # Draw the approximating parabolic curve
    axes[1].plot(x_p, y_p, 'g--', lw=1.5)

# Mark the discrete evaluation nodes with green circles
axes[1].plot(x_nodes, y_nodes, 'go', label='Integration Nodes')
axes[1].set_title("Composite Simpson's 1/3 Rule (n=4)")
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].grid(True)
axes[1].legend()

# Adjust layout spacing and display the final plots
plt.tight_layout()
plt.show()
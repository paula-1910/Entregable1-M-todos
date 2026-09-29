def newton_raphson(f, df, p0, tol, max_iter=100):
    # Initialize the current point with the initial approximation p0
    p = p0
    
    # Loop for a maximum number of iterations to avoid infinite execution
    for i in range(1, max_iter + 1):
        # Evaluate the target function f(p) and its first derivative df(p) at current point p
        f_val = f(p)
        df_val = df(p)
        
        # Check if the derivative is zero to prevent division by zero (tangent line becomes horizontal)
        if df_val == 0:
            raise ValueError("Derivative is zero. Method failed.")
            
        # Newton-Raphson update formula: p_{n+1} = p_n - f(p_n) / f'(p_n)
        p_next = p - f_val / df_val
        
        # Stopping criterion: if the absolute difference between successive approximations
        # |p_{n+1} - p_n| is less than the tolerance, convergence has been reached
        if abs(p_next - p) < tol:
            return p_next, i  # Return the approximate root and iteration count
        
        # Update the point for the next iteration
        p = p_next
        
    # Return current approximation if maximum iterations are reached without meeting tolerance
    return p, max_iter

# Define the target function f(x) = x^3 - 2x - 2 and its derivative f'(x) = 3x^2 - 2
f = lambda x: x**3 - 2*x - 2
df = lambda x: 3*x**2 - 2

# Compute the root using the initial guess p0 = 1.5 for tolerance 10^-3
root_1e3, iter_1e3 = newton_raphson(f, df, 1.5, 1e-3)

# Compute the root using the initial guess p0 = 1.5 for tolerance 10^-5
root_1e5, iter_1e5 = newton_raphson(f, df, 1.5, 1e-5)

# Display the results
print(f"Tol 10^-3 -> Root: {root_1e3:.6f}, Iterations: {iter_1e3}")
print(f"Tol 10^-5 -> Root: {root_1e5:.6f}, Iterations: {iter_1e5}")
import pandas as pd

# Define the function f(x) = x^3 - 2x - 2
def f(x):
    return x**3 - 2*x - 2

# Define the first derivative f'(x) = 3x^2 - 2
def df(x):
    return 3*x**2 - 2

def newton_raphson(p0, tol, max_iter=100):
    """
    Implements the Newton-Raphson method to find a root of f(x) = 0.
    
    Parameters:
    - p0: Initial guess
    - tol: Tolerance limit for stopping criterion |p_k - p_{k-1}| < tol
    - max_iter: Maximum allowed iterations to prevent infinite loops
    
    Returns:
    - p_curr: Estimated root value
    - iterations: Number of iterations performed
    """
    p_curr = p0
    for iteration in range(1, max_iter + 1):
        f_val = f(p_curr)
        df_val = df(p_curr)
        
        # Check to avoid division by zero if derivative is zero
        if df_val == 0:
            raise ValueError("Derivative is zero. Method failed.")
            
        # Newton-Raphson updating formula: p_{n+1} = p_n - f(p_n) / f'(p_n)
        p_next = p_curr - f_val / df_val
        
        # Check convergence condition based on the tolerance
        if abs(p_next - p_curr) < tol:
            return p_next, iteration
            
        p_curr = p_next
        
    return p_curr, max_iter

# Initial approximations and tolerances specified in the exercise
initial_guesses = [1.5, 2.5]
tolerances = [1e-3, 1e-5]

results = []

# Perform numerical calculations for each combination of initial guess and tolerance
for p0 in initial_guesses:
    for tol in tolerances:
        root, iterations = newton_raphson(p0, tol)
        results.append({
            "p0": p0,
            "Tolerance": tol,
            "Approximated Root": round(root, 6),
            "Iterations": iterations
        })

# Display results in a clear structured table
df_results = pd.DataFrame(results)
print(df_results.to_string(index=False))
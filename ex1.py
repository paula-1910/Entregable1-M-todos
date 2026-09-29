def bisection(f, a, b, tol):
    # Check the initial condition for Bolzano's Theorem:
    # The function must have opposite signs at the interval endpoints [a, b].
    # If f(a) * f(b) >= 0, both values share the same sign, so a root cannot be guaranteed.
    if f(a) * f(b) >= 0:
        raise ValueError("The interval does not satisfy Bolzano's theorem (no sign change).")
    
    # Counter to keep track of the total number of iterations executed
    iter_count = 0
    
    # Stopping criterion: continue halving the interval as long as half of its length
    # (which represents the maximum bound on the absolute error) is greater than the tolerance.
    while (b - a) / 2.0 > tol:
        iter_count += 1
        
        # Calculate the midpoint of the current interval
        c = (a + b) / 2.0
        
        # Ideal case: if the midpoint happens to be the exact root, stop early
        if f(c) == 0:
            return c, iter_count
        
        # Determine which subinterval contains the root:
        # If f(a) and f(c) have opposite signs, the root lies in [a, c]
        elif f(a) * f(c) < 0:
            b = c  # Update the upper bound
        # Otherwise, f(c) and f(b) have opposite signs, so the root lies in [c, b]
        else:
            a = c  # Update the lower bound
            
    # Upon exiting the loop, perform a final step to compute the 
    # best midpoint estimation within the sufficiently narrowed interval.
    iter_count += 1
    c = (a + b) / 2.0
    return c, iter_count

# Function definition: f(x) = x^3 + x - 3
f = lambda x: x**3 + x - 3

# Case 1: Run the bisection algorithm with a tolerance of 10^-3 in the interval [1.0, 1.5]
root1, iter1 = bisection(f, 1.0, 1.5, 1e-3)
print(f"Tol 10^-3 -> Root approx: {root1:.6f}, Iterations: {iter1}")

# Case 2: Run the bisection algorithm with a tolerance of 10^-5 in the same interval
root2, iter2 = bisection(f, 1.0, 1.5, 1e-5)
print(f"Tol 10^-5 -> Root approx: {root2:.6f}, Iterations: {iter2}")
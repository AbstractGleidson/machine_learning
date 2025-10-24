from linearFuction import linearFunction

def gradient(x, y, a=0, b=0, learn=1.0e-3, steps=1000):
    """

    Args:
        x (array of numbers): array of numbers for axis x
        y (array of numbers): array of numbers for axis y
        a (number): coefficient a 
        b (number): coefficient b
        learn (number, optional): Size step of learning. Defaults to 1.0e-2.
        alfa (int, optional): Numbers of interactions. Defaults to 1000.

    Returns:
        a, b: adjusted coefficients
    """
    m = x.shape[0] # number of elements
    
    for i in range(steps):
        # calculates all y points for current coefficient values
        f_ab = linearFunction(x, a, b) 
         
        grad_a = 0 # Gradient sum for the coefficient a
        grad_b = 0 # Gradient sum for the coefficient b
        
        for j in range(m):
            # erro calculation
            error = f_ab[j] - y[j]
            
            grad_a += error * x[j] # increasing the gradient a
            grad_b += error # increasing the gradient b
        
        # update parable coefficients
        a -= (learn / m) * grad_a # gradient avarege for a 
        b -= (learn / m) * grad_b # gradient avarege for b
        
        # Show results 
        if i % 10 == 0:
            print(f"{i:04d}: a={a:.4f}, b={b:.4f}")
            
    return a, b # adjusted coefficients
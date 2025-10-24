from quadraticFuction import quadraticFunction

def gradient_quadratic(x, y, a=0, b=0, c=0, learn=1e-3, steps=1000):
    """
    Args:
        x (array of numbers): array of numbers for axis x
        y (array of numbers): array of numbers for axis y
        a (int, optional): coefficient a. Defaults to 0.
        b (int, optional): coefficient b. Defaults to 0.
        c (int, optional): coefficient c. Defaults to 0.
        learn (small number, optional): Size step of learning. Defaults to 1e-3.
        steps (int, optional): Numbers of interactions. Defaults to 1000.

    Returns:
        a, b, c: adjusted coefficients
    """
    
    m = x.shape[0] # number of elements
    
    for i in range(steps):
        
        # calculates all y points for current coefficients values
        f_abc = quadraticFunction(x, a, b, c)
        
        grad_a = 0 # Gradient sum for the coefficient a
        grad_b = 0 # Gradient sum for the coefficient b
        grad_c = 0 # Gradient sum for the coefficient c
        
        for j in range(m):
            # erro calculation
            error = f_abc[j] - y[j]
            
            grad_a += error * (x[j]**2) # increasing the gradient a
            grad_b += error * x[j] # increasing the gradient b
            grad_c += error # increasing the gradient c
        
        # updata parable coefficients
        a -= (learn / m) * grad_a # gradient avarege for a
        b -= (learn / m) * grad_b # gradient avarege for b
        c -= (learn / m) * grad_c # gradient avarege for c
        
        # show results
        if i % 100 == 0:
            print(f"{i:04d}: a= {a:.4f}, b= {b:.4f}, c= {c:.4f}")
    
    return a, b, c

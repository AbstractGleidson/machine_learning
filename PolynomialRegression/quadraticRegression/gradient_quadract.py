from quadraticFuction import quadraticFunction
import numpy

def gradient_quadratic(a, b, c, x_values, y_values, learn=1e-3, steps=10000):
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
    x_values = numpy.array(x_values)
    y_values = numpy.array(y_values)
    m = x_values.shape[0]

    for i in range(steps):
        
        # calculates all y points for current coefficients values
        f_abc = quadraticFunction(a, b, c, x_values)
        error = f_abc - y_values
    
        grad_a = numpy.dot(error, (x_values ** 2)) # Gradient sum for the coefficient a
        grad_b = numpy.dot(error, x_values) # Gradient sum for the coefficient b
        grad_c = numpy.sum(error) # Gradient sum for the coefficient 
        
        # updata parable coefficients
        a -= (learn / m) * grad_a # gradient avarege for a
        b -= (learn / m) * grad_b # gradient avarege for b
        c -= (learn / m) * grad_c # gradient avarege for c
        
        # show results
        if i % 100 == 0:
            print(f"{i:04d}: a= {a:.4f}, b= {b:.4f}, c= {c:.4f}")
    
    return a, b, c

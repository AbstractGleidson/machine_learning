from quadraticFuction import quadraticFunction
import numpy

def costFuction(a, b, c, x_values, y_values):
    """
    Args:
        x (array of numbers): arrays of numbers for axis x
        y (array of numbers): arrays of numbers for axis y
        a (number): coefficient a 
        b (number): coefficient b
        c (number): coefficitent c

    Returns:
        number: Sum of cost
    """
    
    x_values = numpy.array(x_values)
    # calculates all y points for cofficients values
    f_abc = quadraticFunction(a, b, c, x_values) 
    cost_sum = numpy.mean((f_abc - y_values) ** 2)
    
    return cost_sum # cost 
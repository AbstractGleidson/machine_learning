from linearFuction import linearFunction
import numpy

def costFuction(a, b, x_values, y_values):
    """_

    Args:
        a (number): coefficient a 
        b (number): coefficient b
        x (numpy array): arrays of numbers for axis x
        y (numpy array): arrays of numbers for axis y

    Returns:
        cost: Sum of cost
    """
    
    x_values = numpy.array(x_values)
    y_values = numpy.array(y_values)
    
    f_ab = linearFunction(a, b, x_values) 
    cost = numpy.mean((f_ab - y_values) ** 2) # Sum of Squared Error
    
    return cost 
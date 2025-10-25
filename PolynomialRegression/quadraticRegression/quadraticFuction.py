import numpy

def quadraticFunction(a, b, c, x_values):
    """
    Args:
        x (array of numbers): values on the x-axis
        a (number): a coefficient of the parable
        b (number): b coefficient of the parable
        c (number): c coefficient of the parable

    Returns:
        f(x) = ax**2 + bx + c  
    """
    
    x_values = numpy.array(x_values)
    predicts = ((x_values**2) * a) + (x_values * b) + c # array of predicts on the y-axis
    
    return predicts

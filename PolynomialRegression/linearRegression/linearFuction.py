import numpy

def linearFunction(a, b, x_values):
    """
    Args:
        a (number): angular coefficient of the line
        b (number): linear coefficient of the line
        x_values (numpy array): values on the x-axis

    Returns:
        f_ab (numpy array):  values on the y-axis
    """
    
    x_values = numpy.array(x_values)
    
    f_ab = (a * x_values) + b   # array of predicts values on the y-axis
    return f_ab
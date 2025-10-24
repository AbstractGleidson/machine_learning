import numpy

def quadraticFunction(x, a=0, b=0, c=0):
    """
    Args:
        x (array of numbers): values on the x-axis
        a (number): a coefficient of the parable
        b (number): b coefficient of the parable
        c (number): c coefficient of the parable

    Returns:
        f(x) = ax**2 + bx + c  
    """
    m = x.shape[0] # number of elements x
    predicts = [0] * m # array of predicts on the y-axis
    
    for i in range(m):
        y = (a * x[i]**2) + (b * x[i]) + c # equation of the parable
        
        predicts[i] = y
        
    return numpy.array(predicts)

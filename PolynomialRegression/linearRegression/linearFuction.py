import numpy

def linearFunction(x, a = 0, b = 0):
    """
    Args:
        a (number): angular coefficient of the line
        b (number): linear coefficient of the line
        values (array of numbers): values on the x-axis

    Returns:
        predicts (array numbers):  values on the y-axis
    """
    
    m = x.shape[0] # number of elements x
    predicts = [0] * m  # array of predicts values on the y-axis
    
    for i in range(m):
        y = (a * x[i]) + b # equation of the line 
        
        predicts[i] = y
    
    return numpy.array(predicts)
# Implementing the function model linear
# for linear regression with one variable
import numpy 
import matplotlib.pyplot as pyplot

def computer_model_output(x, w, b):
    """
    Computes the prediction of linear model

    Args:
        x (ndarray(m,)): Data, m examples
        w (scalar): model parameters
        b (scalar): model parameters

    Returns:
        f_wb: (ndarray(m,)): model prediction
    """
    
    m = x.shape[0] # size ndarray x
    f_wb = numpy.zeros(m) # Same [0] * m
    
    for i in range(m):
        f_wb[i] = (w * x[i]) + b
    
    return f_wb


# Data Training 
#  size(1 000 m²)  |  prince (1 000 R$)
#         1        |       300 
#         2        |       500 

# Seting Data Training 
x_train = numpy.array([1.0, 2.0, 3.0]) # Array for feature
y_train = numpy.array([300.0, 500.0, 700.0]) # Array for target

# m number of training examples 
m = x_train.shape[0] # return size of array x_train
# Or m = len(x_train)

# Parameters of function model linear 
# W - coefficient of the line 
# b - angular coefficient
w = 200 
b = 100 

f_wb = computer_model_output(x_train, w, b) # Predictis 

pyplot.plot(x_train, f_wb, c='b', label='Predições') # draw line between points

# Plotting the data 
pyplot.scatter(x_train, y_train, marker='x', c='r', label='Valores atuais') # define two points of datas, extremities
pyplot.title("Preço das casas")
pyplot.ylabel("Preço (1 000 R$)") # Label on axle y
pyplot.xlabel("Tamanho (1 000 m²)") # Label on axle x
pyplot.legend() # add legend with labels
pyplot.show()
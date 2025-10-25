from quadraticFuction import quadraticFunction
from costFuction import costFuction
from gradient_quadract import gradient_quadratic
import matplotlib.pyplot as pyplot
import numpy 

if __name__ == "__main__":
    x_values = numpy.arange(0, 21, dtype=float)
    f_abc = quadraticFunction(2, 5, 10, x_values)
    x_points = [x_values[0], x_values[x_values.shape[0] // 2], x_values[-1]]
    f_abc_points = [f_abc[0], f_abc[x_values.shape[0] // 2], f_abc[-1]]
    
    print(f"\nX: {x_values}")
    print(f"\nF1: {f_abc}")
    print(f"\nCusto: {costFuction(2, 5, 10, x_values, f_abc)}")
    
    # Ajuste via gradiente 
    x_g = numpy.arange(0, 21, dtype=float)
    
    print(f"Valores de G: {x_g}")
    y_g = quadraticFunction(3, 6, 20, x_g)
    a, b, c =  gradient_quadratic(0, 0, 0, x_g, y_g, 1.0e-5, 2500000)
    print(f"\nCoeficientes ajustados: a = {a} - b = {b} - c = {c}\n")
    
    pyplot.plot(x_values, f_abc, color="blue", ls="--")
    pyplot.scatter(x_points, f_abc_points, color="blue")
    
    pyplot.plot(x_g, quadraticFunction(a, b, c, x_g), ls="--", color="red")
    pyplot.scatter(x_g, y_g, color="red")
    pyplot.show()
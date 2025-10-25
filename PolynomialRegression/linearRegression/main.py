from linearFuction import linearFunction
from costFuction import costFuction
from gradient import gradient
import matplotlib.pyplot as pyplot
import numpy

if __name__ == "__main__":
    x_values = numpy.arange(1, 31, dtype=float)
    
    media = numpy.mean(x_values)
    soma = numpy.sum(x_values)
    
    f_ab1 = linearFunction(media, soma, x_values=x_values)
    f_ab2 = linearFunction(soma, media, x_values=x_values)
    
    print(f"\nMedia: {media}\nSoma: {soma}")
    print(f"\nX: {x_values}")
    print(f"\nF1: {f_ab1}")
    print(f"\nF2: {f_ab2}")
    
    print(f"\nCusto: {costFuction(200, 100, [1,2], [300, 500])}")
    
    # Ajuste via gradiente 
    x_values_g = numpy.arange(0, 31, 5, dtype=float)
    
    print(f"Valores de G: {x_values_g}")
    y_values_g = linearFunction(50, 60, x_values_g)
    a, b =  gradient(x_values_g, y_values_g, 0, 0, 1.0e-3, 100000)
    print(f"\nCoeficientes ajustados: a = {a} - b = {b}\n")
    
    pyplot.plot(x_values, f_ab1, ls="--", color="blue") # Plotar linhas
    pyplot.scatter([x_values[0], x_values[x_values.shape[0]//2], x_values[-1]], [f_ab1[0], f_ab1[f_ab1.shape[0]//2], f_ab1[-1]], color="blue") # Plotar pontos
    
    pyplot.plot(x_values_g, linearFunction(a, b, x_values_g), ls="--", color="red")
    pyplot.scatter(x_values_g, y_values_g, color="red")
    # pyplot.plot(x_values, f_ab2, ls="--", color="red")
    # pyplot.scatter([x_values[0], x_values[x_values.shape[0]//2], x_values[-1]], [f_ab2[0], f_ab2[f_ab2.shape[0]//2], f_ab2[-1]], color="red")
    pyplot.show()
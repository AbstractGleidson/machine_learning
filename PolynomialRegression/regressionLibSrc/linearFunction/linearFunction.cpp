#include "linearFunction.h"
#include <vector>

// Calcula valores lineares: y = a*x + b
std::vector<double> linearFunction(const std::vector<double>& x_values, double a, double b)
{
    std::vector<double> y_values;
    y_values.reserve(x_values.size());  // otimização: já aloca espaço

    for (double x : x_values)
    {
        double y = (a * x) + b; 
        y_values.push_back(y); // Adiciona o resultado da função linear
    }

    return y_values;
}

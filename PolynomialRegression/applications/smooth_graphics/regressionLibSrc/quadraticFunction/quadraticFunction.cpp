#include "quadraticFunction.h"
#include <vector>
#include <cmath>

// Calcula valores quadráticos: y = a*x^2 + b*x + c
std::vector<double> quadraticFunction(const std::vector<double>& x_values, double a, double b, double c)
{
    std::vector<double> y_values;
    y_values.reserve(x_values.size());  // evita realocações desnecessárias

    for (double x : x_values)
    {
        double y = (a * std::pow(x, 2)) + (b * x) + c; 
        y_values.push_back(y); // adiciona o resultado da função quadrática
    }

    return y_values;
}

#include "linearGradient.h"
#include "../linearFunction/linearFunction.h"
#include <vector>
#include <array>
#include <cmath> 

// gradientLinear: calcula gradiente para regressão linear
std::array<double, 2> gradientLinear(
    const std::vector<double>& x_values, 
    const std::vector<double>& y_values, 
    double a, 
    double b, 
    double learn, 
    int steps)
{
    int m = x_values.size();

    for (int i = 0; i < steps; i++)
    {
        // Calcula valores atuais da função linear
        std::vector<double> f_ab = linearFunction(x_values, a, b);

        double grad_a = 0.0;
        double grad_b = 0.0;

        for (int j = 0; j < m; j++)
        {
            double error = f_ab[j] - y_values[j];            
            grad_a += error * x_values[j];
            grad_b += error;
        }

        a -= (learn / m) * grad_a;
        b -= (learn / m) * grad_b;
    }

    return {a, b}; // coeficientes ajustados
}
#include "quadraticGradient.h"
#include "../quadraticFunction/quadraticFunction.h" 
#include <vector>
#include <array>
#include <cmath>

// Gradiente para regressão quadrática
std::array<double, 3> gradientQuadratic(
    const std::vector<double>& x_values, 
    const std::vector<double>& y_values, 
    double a, double b, double c, 
    double learn, int steps)
{
    int m = x_values.size();

    for (int i = 0; i < steps; i++)
    {
        std::vector<double> f_abc = quadraticFunction(x_values, a, b, c);

        double grad_a = 0.0;
        double grad_b = 0.0;
        double grad_c = 0.0;
        
        for (int j = 0; j < m; j++)
        {
            double error = f_abc[j] - y_values[j];
            grad_a += error * std::pow(x_values[j], 2);
            grad_b += error * x_values[j];
            grad_c += error; 
        }

        a -= (learn / m) * grad_a;
        b -= (learn / m) * grad_b;
        c -= (learn / m) * grad_c;

        // if(i % 100 == 0)
        //     std::cout << "a=" << a << " b=" << b << " c=" << c << "\n";
    }

    return {a, b, c};
}
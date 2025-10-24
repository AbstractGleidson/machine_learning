#include "quadraticCostFunction.h"
#include "../quadraticFunction/quadraticFunction.h"
#include <vector>
#include <cmath>

// Função de custo para regressão quadrática (MSE)
double costFunctionQuadratic(
    const std::vector<double>& x_values, 
    const std::vector<double>& y_values, 
    double a, double b, double c
)
{
    int m = x_values.size();
    std::vector<double> f_abc = quadraticFunction(x_values, a, b, c);

    double cost_sum = 0.0;

    for (int i = 0; i < m; i++)
    {
        cost_sum += std::pow(f_abc[i] - y_values[i], 2); 
    }

    return cost_sum / m; // custo médio
}

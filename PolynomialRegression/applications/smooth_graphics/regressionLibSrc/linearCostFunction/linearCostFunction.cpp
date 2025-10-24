#include "linearCostFunction.h"
#include "../linearFunction/linearFunction.h"
#include <vector>
#include <cmath>

// Função de custo para regressão linear (MSE)
double costFunctionLinear(const std::vector<double>& x_values, const std::vector<double>& y_values, double a, double b)
{
    int m = x_values.size(); // número de elementos
    std::vector<double> f_ab = linearFunction(x_values, a, b);

    double cost_sum = 0.0;

    for (int i = 0; i < m; i++)
    {
        cost_sum += std::pow(f_ab[i] - y_values[i], 2); 
    }

    return cost_sum / m; // custo médio
}

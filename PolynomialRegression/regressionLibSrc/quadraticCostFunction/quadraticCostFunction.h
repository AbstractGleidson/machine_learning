#pragma once
#include <vector>
#include <cmath>

// Função de custo para regressão quadrática (MSE)
double costFunctionQuadratic(
    const std::vector<double>& x_values, 
    const std::vector<double>& y_values, 
    double a, 
    double b, 
    double c);

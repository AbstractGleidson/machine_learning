#pragma once
#include <vector> // Para arrays dinâmicos
#include <cmath> 

// Função de custo para regressão linear (MSE)
double costFunctionLinear(const std::vector<double>& x_values, const std::vector<double>& y_values, double a, double b);

#pragma once
#include <vector> // para arrays dinâmicos
#include <array>  // para arrays estáticos
#include <cmath> 

// Gradiente para regressão linear
std::array<double, 2> gradientLinear(
    const std::vector<double>& x_values, 
    const std::vector<double>& y_values, 
    double a, 
    double b, 
    double learn, 
    int steps
);

#pragma once
#include <vector> // para arrays dinâmicos
#include <array>  // para arrays estáticos
#include <cmath>  

// Gradiente para regressão quadrática
std::array<double, 3> gradientQuadratic(
    const std::vector<double>& x_values, 
    const std::vector<double>& y_values, 
    double a, 
    double b, 
    double c, 
    double learn, 
    int steps
);

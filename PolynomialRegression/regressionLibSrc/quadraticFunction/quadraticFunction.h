#pragma once
#include <vector>
#include <cmath>

// Calcula valores quadráticos: y = a*x^2 + b*x + c
std::vector<double> quadraticFunction(
    const std::vector<double>& x_values, 
    double a, 
    double b, 
    double c
);

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "linearFunction/linearFunction.h"
#include "linearCostFunction/linearCostFunction.h"
#include "linearGradient/linearGradient.h"
#include "quadraticFunction/quadraticFunction.h"
#include "quadraticCostFunction/quadraticCostFunction.h"
#include "quadraticGradient/quadraticGradient.h"


// faz as conversoes do c++ para o python usando pybind
namespace py = pybind11;

PYBIND11_MODULE(regressionLib, m)
{
    m.doc() = "Biblioteca com funções para implementar regressão linear e quadrática";

    // Funções lineares
    m.def("linearFunction", &linearFunction, 
          "Função linear: y = a*x + b, retorna um vetor de valores y");
    m.def("costFunctionLinear", &costFunctionLinear, 
          "Função de custo para regressão linear (MSE)");
    m.def("gradientLinear", &gradientLinear, 
          "Gradiente para minimizar função de custo linear");

    // Funções quadráticas
    m.def("quadraticFunction", &quadraticFunction, 
          "Função quadrática: y = a*x^2 + b*x + c, retorna um vetor de valores y");
    m.def("costFunctionQuadratic", &costFunctionQuadratic, 
          "Função de custo para regressão quadrática (MSE)");
    m.def("gradientQuadratic", &gradientQuadratic, 
          "Gradiente para minimizar função de custo quadrática");
}

from setuptools import setup, Extension
import pybind11

# Encapsula os pacotes e gera o .pyd da biblioteca
sources = [
    "regressionLibSrc/linearCostFunction/linearCostFunction.cpp",
    "regressionLibSrc/linearFunction/linearFunction.cpp",
    "regressionLibSrc/linearGradient/linearGradient.cpp",
    "regressionLibSrc/quadraticCostFunction/quadraticCostFunction.cpp",
    "regressionLibSrc/quadraticFunction/quadraticFunction.cpp",
    "regressionLibSrc/quadraticGradient/quadraticGradient.cpp",
    "regressionLibSrc/bindings.cpp" 
]

ext_modules = [
    Extension(
        "regressionLib",
        sources,
        include_dirs=[pybind11.get_include(), "regressionLib"],
        language="c++",
    )
]

setup(
    name="RegressionLib",
    description="Biblioteca com funções para regressão linear e quadrática",
    ext_modules=ext_modules,
)

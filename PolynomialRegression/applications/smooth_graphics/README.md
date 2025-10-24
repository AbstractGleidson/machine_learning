# Suavização de Curvas com Regressão Polinomial
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![C++](https://img.shields.io/badge/c++-17-blue.svg)
![Matplotlib](https://img.shields.io/badge/matplotlib-3.7-orange.svg)

Este projeto tem como objetivo demonstrar a aplicação prática da **regressão polinomial de segunda ordem** como método de **suavização e previsão de dados experimentais**.

Como contexto de aplicação, foram utilizados **dados de desempenho de algoritmos de ordenação**, obtidos em um trabalho desenvolvido na disciplina de Estrutura de Dados:  
[https://github.com/AbstractGleidson/AlgoritmosOrdenacao](https://github.com/AbstractGleidson/AlgoritmosOrdenacao)

# Ferramentas

O projeto faz uso de algumas ferramentas e bibliotecas fundamentais para **cálculo, processamento de dados e visualização**:

---

- [**C++**](https://devdocs.io/cpp/) : Utilizado para implementar a **parte de cálculo pesado da regressão quadrática**. Compilado como biblioteca Python usando **Pybind11**, gerando um módulo `.pyd` que pode ser chamado diretamente pelo Python.  

- [**NumPy**](https://numpy.org/): Biblioteca Python para **cálculos numéricos e manipulação de arrays**.

- [**Matplotlib**](https://matplotlib.org/stable/users/index.html): Biblioteca Python para **visualização de dados e gráficos**.  

- [**Python**](https://www.python.org/): Linguagem principal que integra todos os componentes do projeto: coleta de dados, chamada da biblioteca C++ e geração de gráficos.  


# Regresão 
A **regressão polinomial de grau 2** busca ajustar uma função da forma:

$$
f(x) = a x^2 + b x + c
$$

de modo que o **erro quadrático médio** entre os pontos reais $(x_i, y_i)$ e os valores previstos $f(x_i)$ seja minimizado.

No projeto, os coeficientes $a$, $b$ e $c$ são obtidos por meio do **gradiente descendente**, um método iterativo que ajusta os parâmetros na direção de menor erro:

$$
\begin{aligned}
a &:= a - \alpha \frac{\partial J}{\partial a},\\[4pt]
b &:= b - \alpha \frac{\partial J}{\partial b},\\[4pt]
c &:= c - \alpha \frac{\partial J}{\partial c},
\end{aligned}
$$

onde:

- $J(a, b, c)$ é a **função de custo** (erro médio quadrático);
- $\alpha$ é a **taxa de aprendizado**.

# Implementação
Para aumentar a performance do cálculo da regressão quadrática, a parte de cálculo do gradiente e da função quadrática foi implementada em C++.

 - A biblioteca é compilada como um módulo Python usando Pybind11, gerando um arquivo .pyd que é importável diretamente no Python.

 - Essa abordagem reduz drasticamente o tempo de cálculo, tendo em vista a quantidade de operações necessarias para minimizar a funcao de custo.

# Estrutura

- get_data.py coleta e formata os dados.

 - main.py chama a biblioteca regressionLib para calcular os coeficientes a, b e c via gradiente descendente em C++.

- Os valores previstos são gerados e plotados usando Matplotlib, mostrando curvas suavizadas sobre os pontos reais.
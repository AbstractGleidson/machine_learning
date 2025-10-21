import matplotlib.pyplot as plt
import numpy as np
import regressionLib.regressionLib as reg
from get_data import getData

# Guarda todos os dados
dados = {
    "bubble": getData("bubble_sort"),
    "insertion": getData("insertion_sort"),
    "selection": getData("selection_sort")
}

for algoritmo, valor_algoritmo in dados.items():
    x_origin = []
    y_origin = []
    
    # Pega os dados de cada algoritmo
    for x, y in valor_algoritmo.items():
        x_origin.append(x)
        y_origin.append(y)

    # Converte para numpy arrays
    x_origin = np.array(x_origin, dtype=float)
    y_origin = np.array(y_origin, dtype=float)

    # Cria novos valores x para previsão
    x_novos = np.arange(x_origin[0], x_origin[-1] + 1, 50)

    # Normaliza, diminue os valores para nao estourar o gradiente
    x_origin /= 1000
    y_origin /= 1000
    x_novos /= 1000

    print(f"Valores x: {x_origin}")
    print(f"Valores y: {y_origin}")
    print(f"Valores x novos: {x_novos}")

    # Converte para listas, para nao dar conflito com regressionLib
    x_origin_list = x_origin.tolist()
    y_origin_list = y_origin.tolist()
    x_novos_list = x_novos.tolist()

    # Regressão quadrática
    a, b, c = reg.gradientQuadratic(
        x_origin_list,
        y_origin_list,
        0, 0, 0,
        1.0e-2,
        3000000
    )

    y_novos = reg.quadraticFunction(x_novos_list, a, b, c)

    print(f"Coeficientes ajustados: a = {a}, b = {b}, c = {c}")
    print(f"Valores previstos: {y_novos}")

    # Desfaz normalização
    x_origin *= 1000
    y_origin *= 1000
    x_novos *= 1000
    y_novos = np.array(y_novos) * 1000

    # Formaliza os dados para plotar no grafico
    dados[algoritmo] = {
        "x_origin": x_origin,
        "y_origin": y_origin,
        "x_novos": x_novos,
        "y_novos": y_novos
    }

# Cores para cada algoritmo no grafico
colors = {
    "bubble": "blue",
    "selection": "red",
    "insertion": "green"
}

# Plotando cada algoritmo no grafico
for k, v in dados.items():
    plt.scatter(v["x_origin"], v["y_origin"], color=colors[k], label="valores reais")
    plt.plot(v["x_novos"], v["y_novos"], ls="--", label=f"{k}", color=colors[k])

plt.xlabel("Número de elementos (n * 1000)")
plt.ylabel("Tempo de execução (ms)")
plt.title("Comparação - Algoritmos de ordenação")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
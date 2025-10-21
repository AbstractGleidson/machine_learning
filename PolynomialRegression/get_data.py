from pathlib import Path
import json

def getData(algorithm) -> dict:
        tam = [100, 250, 500]
        dados = {}
        for i in range(3):
            soma = 0
            arquivo_json = Path.home() / "programacao" / "python" / "machine_learning" / "PolynomialRegression" / "data_base" / algorithm / f"{algorithm}_{tam[i]}.json"
            
            with open(arquivo_json, "r", encoding="utf-8") as f:
                data = json.load(f)
            for j in range (len(data)):
                soma += data[j]["tempo"]
            dados[tam[i]] = (soma/len(data))
        return dados
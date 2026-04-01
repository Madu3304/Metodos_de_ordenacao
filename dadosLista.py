import json
import random

tamanhos = [1000, 5000, 10000, 50000]
usandoDadosDesordenados = {}

for tam in tamanhos:
    usandoDadosDesordenados[f"vetor_{tam}"] = [random.randint(0, 100000) for _ in range(tam)]
nomearquivo = "dadosDesordenacao.json" #salvando

try:
    with open(nomearquivo, 'w') as arquivo_json:
        json.dump(usandoDadosDesordenados, arquivo_json, indent=4)
    print(f"Sucesso! Arquivo '{nomearquivo}' gerado com todos os vetores.")
except Exception as e:
    print(f"Erro ao salvar o arquivo: {e}")
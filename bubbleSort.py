from datadog import initialize, statsd
import time

# 1. Inicialize a conexão com o Agente local
options = {
    'statsd_host': '127.0.0.1',
    'statsd_port': 8125
}
initialize(**options)

def bubbleSort(dadosLista):
    comparacoes = 0 #testar o Open
    trocas = 0

    n = len(dadosLista)

    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes += 1  
            if dadosLista[j] > dadosLista[j + 1]:
                dadosLista[j], dadosLista[j + 1] = dadosLista[j + 1], dadosLista[j]

    return dadosLista, comparacoes, trocas

# Para verificar as paradas adicionei os pontos:
#comparacoes e trocas
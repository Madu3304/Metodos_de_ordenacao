from datadog import initialize, statsd
import time

# 1. Inicialize a conexão com o Agente local
options = {
    'statsd_host': '127.0.0.1',
    'statsd_port': 8125
}
initialize(**options)

def insertionSort(array):
    comparacoes = 0
    trocas = 0

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1

            if array[j] > key:
                array[j + 1] = array[j]
                trocas += 1
                j -= 1
            else:
                break

        array[j + 1] = key

    return array, comparacoes, trocas

# Para verificar as paradas adicionei os pontos:
#comparacoes e trocas
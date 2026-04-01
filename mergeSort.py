from datadog import initialize, statsd
import time

# 1. Inicialize a conexão com o Agente local
options = {
    'statsd_host': '127.0.0.1',
    'statsd_port': 8125
}
initialize(**options)

def mergeSort(dadosLista):
    if len(dadosLista) > 1:
        # aqui dividir
        meio = len(dadosLista) // 2
        esquerda = dadosLista[:meio]
        direita = dadosLista[meio:]

        # aqui ordenar
        mergeSort(esquerda)
        mergeSort(direita)

        comparacoes = 0
        trocas = 0
        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            comparacoes += 1
            if esquerda[i] < direita[j]:
                dadosLista[k] = esquerda[i]
                i += 1  
            else:
                dadosLista[k] = direita[j]
                j += 1
            trocas += 1
            k += 1

        # aqio adicionar o resto
        while i < len(esquerda):
            dadosLista[k] = esquerda[i]
            i += 1
            k += 1
            trocas += 1

        while j < len(direita):
            dadosLista[k] = direita[j]
            j += 1
            k += 1
            trocas += 1

        return dadosLista, comparacoes, trocas
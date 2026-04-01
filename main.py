# from ddtrace import patch_all
# patch_all()

import json
import time
from bubbleSort import bubbleSort
from insertionSort import insertionSort
from mergeSort import mergeSort 
from datadog import initialize, statsd
#usando o OpenTelemetry
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

initialize(statsd_host='127.0.0.1', statsd_port=8125)

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

spanProcessor = SimpleSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(spanProcessor)

with open("dadosDesordenacao.json", "r") as arquivoDados:
    dadosLista = json.load(arquivoDados)

vetorDados = dadosLista["vetor_50000"] #tamanho do dado

# cria 3 listas
dadosbubble = vetorDados.copy() #copy evita que afete um ao outro
dadosinsertion = vetorDados.copy()
dadosmerge = vetorDados.copy()

# Executando os algoritmos sem tempo
# BUBBLE SORT
dadosbubble = vetorDados.copy()
with tracer.start_as_current_span("Bubble Sort") as span:
    _, comp, troc = bubbleSort(dadosbubble)
    span.set_attribute("comparacoes", comp)
    span.set_attribute("trocas", troc)
    
# INSERTION SORT
dadosinsertion = vetorDados.copy()
with tracer.start_as_current_span("Insertion Sort") as span:
    _, comp, troc = insertionSort(dadosinsertion)
    span.set_attribute("comparacoes", comp)
    span.set_attribute("trocas", troc)

# MERGE SORT
dadosmerge = vetorDados.copy()
with tracer.start_as_current_span("Merge Sort") as span:
    _, comp, troc = mergeSort(dadosmerge)
    span.set_attribute("comparacoes", comp)
    span.set_attribute("trocas", troc)

#execultando aqui com tempo
#BUBBLE SORT
dadosbubble = vetorDados.copy()
inicio = time.time()
bubbleSort(dadosbubble)
fim = time.time()
print(f"Bubble Sort: {fim - inicio:.6f} segundos")

#INSERTION SORT 
dadosinsertion = vetorDados.copy()
inicio = time.time()
insertionSort(dadosinsertion)
fim = time.time()
print(f"Insertion Sort: {fim - inicio:.6f} segundos")

#MERGESORT
dadosmerge = vetorDados.copy()
inicio = time.time()
mergeSort(dadosmerge)
fim = time.time()
print(f"Merge Sort: {fim - inicio:.6f} segundos")

# Parametros para ir pro Data Dog
dadosbubble = vetorDados.copy()
with tracer.start_as_current_span("Bubble Sort Datadog") as span:
    inicio = time.time()
    
    _, comp, troc = bubbleSort(dadosbubble)
    
    fim = time.time()
    duracao = fim - inicio

    span.set_attribute("comparacoes", comp)
    span.set_attribute("trocas", troc)
    span.set_attribute("duracao", duracao)

    statsd.gauge('algoritmo.sort.tempo', duracao, tags=["metodo:bubble"])

print(f"[Datadog] Bubble Sort: {duracao:.6f} segundos")


# InsertionSort
dadosinsertion = vetorDados.copy()
with tracer.start_as_current_span("Insertion Sort Datadog") as span:
    inicio = time.time()
    
    _, comp, troc = insertionSort(dadosinsertion)
    
    fim = time.time()
    duracao = fim - inicio

    span.set_attribute("comparacoes", comp)
    span.set_attribute("trocas", troc)
    span.set_attribute("duracao", duracao)

    statsd.gauge('algoritmo.sort.tempo', duracao, tags=["metodo:insertion"])

print(f"[Datadog] Insertion Sort: {duracao:.6f} segundos")


# MergeSort
dadosmerge = vetorDados.copy()
with tracer.start_as_current_span("Merge Sort Datadog") as span:
    inicio = time.time()
    
    _, comp, troc = mergeSort(dadosmerge)
    
    fim = time.time()
    duracao = fim - inicio

    span.set_attribute("comparacoes", comp)
    span.set_attribute("trocas", troc)
    span.set_attribute("duracao", duracao)

    statsd.gauge('algoritmo.sort.tempo', duracao, tags=["metodo:merge"])

print(f"[Datadog] Merge Sort: {duracao:.6f} segundos")

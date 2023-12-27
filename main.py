# coding: utf-8
import math
import numpy as np
import random
import sys
import os
import re
import time
import csv
import Vertice
from Influencia import *

sys.setrecursionlimit(15000)
start_time = time.time()

tamanhoGrafo = int(sys.argv[5])
read_file(int(sys.argv[1]), tamanhoGrafo)
tipo = int(sys.argv[2])
listaSeeds = []
if(tipo == 0):
    tamMaxSeed = int(sys.argv[3])
elif(tipo == 1):
    arqSeed = sys.argv[3]
    read_arq_seed(arqSeed, listaSeedss)
solucao = 0
k = 0
#caso esteja usando o método de encontrar os K vértices mais influentes
if(tipo == 0):
    while(k < tamMaxSeed):
        for i in range(tamanhoGrafo):
            if i not in listaSeeds:
                listaSeeds.append(i)
                aux = calcularSolucao(100, listaSeeds,tamanhoGrafo)
                if aux > solucao:
                    solucao = aux
                    melhorVertice = i
                listaSeeds.remove(i)
        if melhorVertice not in listaSeeds:   
            listaSeeds.append(melhorVertice)
            k +=1
#caso esteja usando o método de encontrar a influência dos vértices semente pré-definidos
elif(tipo == 1):
    solucao = calcular_solucao(100, listaSeedss)

print("Solucao--> ", solucao, "Lista Seed: ", listaSeeds)
tempo_exec = time.time() - start_time
g = float("{:.2f}".format(tempo_exec))
print("Tempo de execucao: ", tempo_exec)

file = 'results.csv'
fieldnames = ['sol', 'tempo_exec', 'tam_solucao','listaSeeds']
if os.path.isfile(file):
    with open(file, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(
            {'sol': solucao, 'tempo_exec': g, 'tam_solucao': len(listaSeeds), 'listaSeeds': listaSeeds})
else:
    with open(file, 'a+', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(
            {'sol': solucao, 'tempo_exec': g, 'tam_solucao': len(listaSeeds), 'listaSeeds': listaSeeds})

from time import process_time
from importlib.metadata import files
from shutil import get_archive_formats
import numpy as np
import random

from greedy_method import calcularRota
from utils import file_reader
from descentHill import descentHill


def simulatedAnnieling(tsp,formato,dimensao):

    S = calcularRota(tsp,formato,dimensao)
    SN = S
    Tempini = 1000

    alpha =  0.001  #coeficiente de resfriamento que varia entra 0% e 100%
    T = Tempini
    interT = 0
    SAmax = 20

    while(T>1):
        while(interT < SAmax):
            interT += 1
            SN = descentHill(tsp, formato, dimensao)
            delta = S[0] - SN[0] # o delta é a subtração das distancias entre o (atual - nova) 
            if(delta > 0):
                S = SN
            else:
                x = random.random()
                if(x < np.exp(-delta/Tempini)): #testa a probabilidade de aceitar a resposta 
                    S = SN
        
        T = alpha * T
        interT = 0
        
    return S[0], S[1]


files = (
    # 'ALL_tsp/bayg29.tsp',
    'ALL_tsp/brazil58.tsp',
    # 'ALL_tsp/brg180.tsp',  #descomentar uma  instancia por vez tanto dessa funcao qnto as outras funcoes tbm 
    # 'ALL_tsp/ts225.tsp',
    # 'ALL_tsp/att48.tsp',
    # 'ALL_tsp/att532.tsp',
    # 'ALL_tsp/bier127.tsp',
)
output = ''


for file in files:
    data = file_reader(file)
    start_time  = process_time()
    results = simulatedAnnieling(data[0],data[1], data[2])
    end_time = process_time()
    output += f' Simulated Annieling Total: distance traveled: {results[0]},  Routes: {str(results[1])}, Execution time: {end_time-start_time:.30f} s\n'
print(output)

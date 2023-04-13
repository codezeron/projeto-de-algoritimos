from importlib.metadata import files
from shutil import get_archive_formats
from time import process_time
from utils import file_reader
import math
#import matplotlib.pyplot as plt
from utils import file_reader

'''
    This

'''


from cmath import inf

def calcularRota (grafo, dimensao, formato):
    
    distancia = 0
    routes = []
    pontos = []

    if(formato == 'EUC_2D' or formato == 'ATT'):
        

        x = 1
        while x < dimensao:
            pontos.append(x)
            x += 1

        start_pos = 0
        next_index = 0
        routes.append(0)
        while len(pontos) > 0:
            distance = -1
            city = 0
            while city < dimensao:
                if distance == -1 and city != start_pos and city in pontos:
                    distance = math.sqrt(pow(grafo[start_pos][0] - grafo[city][0], 2) + 
                                        pow(grafo[start_pos][1] - grafo[city][1], 2))
                    next_index = city
                elif city != start_pos and math.sqrt(pow(grafo[start_pos][0] - grafo[city][0], 2) + 
                                        pow(grafo[start_pos][1] - grafo[city][1], 2)) < distance and city in pontos:
                    
                    distance = math.sqrt(pow(grafo[start_pos][0] - grafo[city][0], 2) + 
                                        pow(grafo[start_pos][1] - grafo[city][1], 2))
                    next_index = city
                city += 1
            pontos.pop(pontos.index(next_index))
            start_pos = next_index
            distancia += distance
            routes.append(next_index )
        distancia += math.sqrt(pow(grafo[start_pos][0]-grafo[0][0],2) + pow(grafo[start_pos][1] - grafo[0][1],2))
        routes.append(0)
    
    if(formato == 'UPPER_ROW'):

        x = 1
        while x < dimensao:
            pontos.append(x)
            x += 1

        start_pos = 0
        next_index = 0
        routes.append(0)
        while len(pontos) > 0:
            distance = -1
            y = 0
            while y < dimensao:
                if distance == -1 and y != start_pos and y in pontos:
                    distance = grafo[start_pos][y]
                    next_index = y
                elif y != start_pos and grafo[start_pos][y] < distance and y in pontos:
                    distance = grafo[start_pos][y]
                    next_index = y
                y += 1
            pontos.pop(pontos.index(next_index))
            start_pos = next_index
            distancia += distance
            routes.append(next_index)
        distancia += grafo[start_pos][0]
        routes.append(0)
    
    return distancia, routes,formato



files = (
    # 'ALL_tsp/bayg29.tsp',
    'ALL_tsp/brazil58.tsp',
    # 'ALL_tsp/brg180.tsp',
    # 'ALL_tsp/ts225.tsp',
    # 'ALL_tsp/att48.tsp',
    # 'ALL_tsp/att532.tsp',
    # 'ALL_tsp/bier127.tsp',
)
output = ''

for file in files:
    data = file_reader(file)
    start_time  = process_time()
    results = calcularRota(data[0], data[1], data[2])
    end_time = process_time()
    output += f' Greedy_methood: distance traveled: {results[0]},  Routes: {str(results[1])}, Execution time: {end_time-start_time:.30f} s\n\n'
print(output)

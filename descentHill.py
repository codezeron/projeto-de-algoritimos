from importlib.metadata import files
from shutil import get_archive_formats
from time import process_time
import math

from greedy_method import calcularRota
from utils import file_reader

start_time  = process_time()

def getNeighbours(solution):
    neighbours  =  []
    
    for i in range(1,len(solution)):
        for j in range(i + 1, len(solution)-1):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    
    return neighbours

def routeLength(tsp, solution,formato,dimensao):
    routeLength = 0
    if(formato == 'UPPER_ROW'):
        for i in range(len(solution)):
            routeLength += tsp[solution[i-1]][solution[i]]
    if(formato == 'EUC_2D' or formato == 'ATT'):
        x = 1
        
        pontos = []
        while x < dimensao:
            pontos.append(x)
            x += 1

        start_pos = 0
        next_index = 0
        
        while len(pontos) > 0:
            distance = -1
            city = 0
            while city < dimensao:
                if distance == -1 and city != start_pos and city in pontos:
                    distance = math.sqrt(pow(tsp[start_pos][0] - tsp[city][0], 2) + 
                                        pow(tsp[start_pos][1] - tsp[city][1], 2))
                    next_index = city
                elif city != start_pos and math.sqrt(pow(tsp[start_pos][0] - tsp[city][0], 2) + 
                                        pow(tsp[start_pos][1] - tsp[city][1], 2)) < distance and city in pontos:
                    
                    distance = math.sqrt(pow(tsp[start_pos][0] - tsp[city][0], 2) + 
                                        pow(tsp[start_pos][1] - tsp[city][1], 2))
                    next_index = city
                city += 1
            pontos.pop(pontos.index(next_index))
            start_pos = next_index
            routeLength += distance
            
        routeLength += math.sqrt(pow(tsp[start_pos][0]-tsp[0][0],2) + pow(tsp[start_pos][1] - tsp[0][1],2))
        
    return routeLength

def getBestNeighbour(tsp, neighbours,formato,dimension):
    bestRouteLength = routeLength(tsp, neighbours[0],formato,dimension)
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(tsp,neighbour,formato,dimension)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    return bestNeighbour, bestRouteLength

def descentHill(tsp, dimension, formato):
    currentRouteLength, currentSolution, form = calcularRota(tsp,dimension, formato)
    neighbours = getNeighbours(currentSolution)

    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours,formato,dimension)

    while bestNeighbourRouteLength > currentRouteLength: 
        bestNeighbour = currentSolution 
        bestNeighbourRouteLength = currentRouteLength
        neighbours = getNeighbours(currentSolution)
        currentSolution, currentRouteLength = getBestNeighbour(tsp, neighbours,formato,dimension)
        
        
    return bestNeighbourRouteLength,bestNeighbour, form

#tem que colocar os parametros de um em um, se nao o algoritimo mistura todos os parametros indesejados com os desejados 
# e nao retornara o resultado esperado

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
    results = descentHill(data[0],data[1], data[2])
    end_time = process_time()
    output += f' Descent Hill Total: distance traveled: {results[0]},  Routes: {str(results[1])}, Execution time: {end_time-start_time:.30f} s\n'
print(output)

    
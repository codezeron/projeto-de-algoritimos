''' Reads a file and returns:
    Graph matrix in array format, dimension, capacity, matrix format, demand array and depot array
'''
def file_reader (path: str):
    graph = list()
    graph_format = ''
   
    with open(path) as file:
        file = file.read()
        file = file.split()
        
        dimension = int(file[file.index('DIMENSION') + 2])

        # Creating a graph for a adjacency matrix that contains the weights of each edge section
        if 'EDGE_WEIGHT_SECTION' in file:
            i = file.index('EDGE_WEIGHT_SECTION') + 1
            try:
                graph_format = str(file[file.index('EDGE_WEIGHT_FORMAT') + 2])
            except:
                graph_format = str(file[file.index('EDGE_WEIGHT_FORMAT:') + 1])
            # Grafo de dimensão d^2 zerado
            for index  in range(dimension):
                line = list()
                for jindex in range(dimension):
                    line.append(0)
                graph.append(line)

            # Creating the graph array
            while file[i] != 'EOF':
                j = 0
                while j < dimension - 1:
                    k = j + 1
                    while k < dimension:
                        graph[j][k] = graph[k][j] = int(file[i])
                        k += 1
                        i += 1
                    j += 1
            i+=1
                    

        # Creating a graph for an euclidean coordinates node display
        elif 'NODE_COORD_SECTION' in file:
            i = file.index('NODE_COORD_SECTION') + 1
            coord = list()
            
            try:
                graph_format = str(file[file.index('EDGE_WEIGHT_TYPE') + 2])
            except: 
                graph_format =  str(file[file.index('EDGE_WEIGHT_TYPE:') + 1])
            
            while file[i] != 'EOF':
                coord.clear()
                coord.append(int(file[i + 1]))
                coord.append(int(file[i + 2]))
                i+=3
                graph.append(tuple(coord))
            i+=1
           
    return graph, dimension, graph_format

#if __name__ == '_main__':
#    graph, dimenion = file_reader('ALL_tsp/bayg29.tsp')
#    print(graph)
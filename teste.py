from readDataFromFile import readFiles
import collections

def teste():
    loader = readFiles("P-n16-k8")
    vertexes = loader.get_vertexes()
    matrix = loader.get_matrix()
    capacity = int(loader.get_capacity())
    dimension = int(loader.get_dimension())

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])
    for key in vertexes:
        vertexes[key] = int(vertexes[key])
    
    print(dimension)
    print(capacity)
    print(vertexes)
    print(matrix)
    
teste()
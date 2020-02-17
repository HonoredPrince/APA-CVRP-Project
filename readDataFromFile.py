class readFiles():
    def __init__(self, filename):
        data = open("instancias_teste/" + filename + ".txt", "r")
        lines = data.readlines()

        self.dimension = 0
        self.capacity = 0

        self.vertexes = {}
        self.matrix = []

        vertexHasContent = False
        matrixHasContent = False

        for line in lines:
            line = line.replace('\n', '')

            if line.__contains__('DIMENSION:'):
                demandLine = line.split()
                self.dimension = demandLine[1]
            
            if line.__contains__('CAPACITY:'):
                capacityLine = line.split()
                self.capacity = capacityLine[1]

            if line.__contains__('DEMAND_SECTION:') or vertexHasContent:
                vertexHasContent = True
                if line.__contains__('DEMAND_SECTION:'):
                    continue
                vertexDemandLine = line.split()
                if(len(vertexDemandLine) == 0):
                    vertexHasContent = False
                else:
                    self.vertexes[vertexDemandLine[0]] = vertexDemandLine[1]
            
            if line.__contains__('EDGE_WEIGHT_SECTION') or matrixHasContent:
                matrixHasContent = True
                if line.__contains__('EDGE_WEIGHT_SECTION'):
                    continue
                matrixLine = line.split()
                if(len(matrixLine) == 0):
                    matrixHasContent = False
                else:
                    self.matrix.append(matrixLine)
            else:
                continue

    def get_vertexes(self):       
        return self.vertexes
    
    def get_matrix(self):       
        return self.matrix
    
    def get_dimension(self):       
        return self.dimension
    
    def get_capacity(self):       
        return self.capacity
            

  


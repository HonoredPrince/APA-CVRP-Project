class readFiles():
    def __init__(self, filename):
        data = open("instancias_teste/" + filename, "r")
        lines = data.readlines()

        self.dimension = 0
        self.capacity = 0

        self.stopPoints = {}
        self.costMatrix = []

        stopPointsHasContent = False
        matrixCostHasContent = False

        for line in lines:
            line = line.replace('\n', '')

            if line.__contains__('DIMENSION:'):
                demandLine = line.split()
                self.dimension = demandLine[1]
            
            if line.__contains__('CAPACITY:'):
                capacityLine = line.split()
                self.capacity = capacityLine[1]

            if line.__contains__('DEMAND_SECTION:') or stopPointsHasContent:
                stopPointsHasContent = True
                if line.__contains__('DEMAND_SECTION:'):
                    continue
                stopPointsDemandLine = line.split()
                if(len(stopPointsDemandLine) == 0):
                    stopPointsHasContent = False
                else:
                    self.stopPoints[stopPointsDemandLine[0]] = stopPointsDemandLine[1]
            
            if line.__contains__('EDGE_WEIGHT_SECTION') or matrixCostHasContent:
                matrixCostHasContent = True
                if line.__contains__('EDGE_WEIGHT_SECTION'):
                    continue
                matrixCostLine = line.split()
                if(len(matrixCostLine) == 0):
                    matrixCostHasContent = False
                else:
                    self.costMatrix.append(matrixCostLine)
            else:
                continue

    def get_stopPoints(self):       
        return self.stopPoints
    
    def get_costMatrix(self):       
        return self.costMatrix
    
    def get_dimension(self):       
        return self.dimension
    
    def get_capacity(self):       
        return self.capacity
            

  


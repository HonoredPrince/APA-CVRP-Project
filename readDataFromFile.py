class readFiles():
    def __init__(self, filename):
        data = open("instancias_teste/" + filename, "r")
        lines = data.readlines()

        #Create variables to receive data from the file
        self.dimension = 0
        self.capacity = 0

        #Used python Dictonary data structure for the point-demand data
        self.stopPoints = {}

        self.costMatrix = []

        #Check if any data is written on the demand a matrix section of the file
        stopPointsHasContent = False
        matrixCostHasContent = False

        #Iterate every line from the file and split the string using the keywords 
        #and store them on the respective variable or location
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

    #Deafault get functions 
    def get_stopPoints(self):       
        return self.stopPoints
    
    def get_costMatrix(self):       
        return self.costMatrix
    
    def get_dimension(self):       
        return self.dimension
    
    def get_capacity(self):       
        return self.capacity
            

  


from readDataFromFile import readFiles
import collections

class NearestNeighbour:
    def __init__(self):
        loader = readFiles("P-n16-k8")
        self.demand = loader.get_vertexes()
        self.matrix = loader.get_matrix()
        self.capacity = int(loader.get_capacity())
        self.dimension = int(loader.get_dimension())

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = int(self.matrix[i][j])
        for key in self.demand:
            self.demand[key] = int(self.demand[key])

        self.truckDestination = {}

    def nearestNeighborFunction(self):
        truckCapacity = self.capacity
        i = 0
        truck = 0
        visitedClients = [0]
        self.truckDestination[truck] = [0]
        totalDistance = 0
        print(self.demand)

        while len(visitedClients) < len(self.demand):
            nearestDistance = 100000
            nearestVertex = i
            truckCanGoNext = False

            for j in range(len(self.matrix[i])):
                if j not in visitedClients and nearestDistance > self.matrix[i][j] and truckCapacity - self.demand[str(j)] >= 0:
                    truckCanGoNext = True
                    nearestVertex = j
                    nearestDistance = self.matrix[i][j]

            if truckCanGoNext:
                truckCapacity = truckCapacity - self.demand[str(nearestVertex)]
                self.truckDestination[truck].append(nearestVertex)
                totalDistance += nearestDistance
                visitedClients.append(nearestVertex)
                if not len(visitedClients) < len(self.demand):
                    self.truckDestination[truck].append(0)
                    totalDistance += self.matrix[nearestVertex][0]
                    self.truckDestination[truck].append(truckCapacity)
                    self.truckDestination[truck].append(totalDistance)
                i = nearestVertex

            else:
                self.truckDestination[truck].append(0)
                totalDistance += self.matrix[nearestVertex][0]
                self.truckDestination[truck].append(truckCapacity)
                self.truckDestination[truck].append(totalDistance)
                truckCapacity = self.capacity

                truck += 1
                totalDistance = 0
                self.truckDestination[truck] = []
                self.truckDestination[truck].append(0)

    def printPaths(self):
        for truck in self.truckDestination:
            print("Truck Number", truck)
            print("Truck vertexes", self.truckDestination[truck][:-2])
            print("Truck Capacity", self.capacity - self.truckDestination[truck][-2])
            print("Traveled distance", self.truckDestination[truck][-1], '\n')



BestInsertionHeuristic = NearestNeighbour()
BestInsertionHeuristic.nearestNeighborFunction()
BestInsertionHeuristic.printPaths()
        
    

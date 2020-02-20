# -*- coding: utf-8 -*-
from readDataFromFile import readFiles
import collections

class NearestNeighbour:
    def __init__(self, instance):
        self.filename = str(instance)
        loader = readFiles(self.filename)
        self.demand = loader.get_stopPoints()
        self.matrix = loader.get_costMatrix()
        self.capacity = int(loader.get_capacity())
        self.dimension = int(loader.get_dimension())
        self.vehicleDestinationHistory = {}

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = int(self.matrix[i][j])
        for key in self.demand:
            self.demand[key] = int(self.demand[key])

    #Ned Flanders(Simpsons) a.k.a "vizinho mais próximo"
    def nearestNedFlanders(self):
        currentClient = 0
        clientsDemandSize = len(self.demand)
        visitedClientsHistory = [0]

        vehicle = 0
        self.vehicleDestinationHistory[vehicle] = [0]
        sumVehicleTravelDistance = 0
        vehicleCapacity = self.capacity
        
        numberOfVertexToCompare = len(self.matrix[currentClient])
        
        while len(visitedClientsHistory) < clientsDemandSize:
            #In the first iteration for every vehicle we only compare deposit location to itself
            #So in order to the 0 distance be accpeted in the if statement, use any fictional value
            #for the distance between Deposit(0) and Deposit(0)
            minDistanceCalculated = 777 
            clientToVisit = currentClient
            vehicleIsOkToProceed = False
        
            for client in range(numberOfVertexToCompare):
                if client not in visitedClientsHistory:
                    if(minDistanceCalculated > self.matrix[currentClient][client]):
                        if(vehicleCapacity - self.demand[str(client)] >= 0):
                            vehicleIsOkToProceed = True
                            clientToVisit = client
                            minDistanceCalculated = self.matrix[currentClient][client]
        
            if vehicleIsOkToProceed:
                vehicleCapacity -= self.demand[str(clientToVisit)]
                sumVehicleTravelDistance += minDistanceCalculated
                visitedClientsHistory.append(clientToVisit)
                self.vehicleDestinationHistory[vehicle].append(clientToVisit)
                if len(visitedClientsHistory) == clientsDemandSize:
                    self.vehicleDestinationHistory[vehicle].append(0)
                    sumVehicleTravelDistance += self.matrix[clientToVisit][0]
                    self.vehicleDestinationHistory[vehicle].append(vehicleCapacity)
                    self.vehicleDestinationHistory[vehicle].append(sumVehicleTravelDistance)
                currentClient = clientToVisit
            else:
                self.vehicleDestinationHistory[vehicle].append(0)
                sumVehicleTravelDistance += self.matrix[clientToVisit][0]
                self.vehicleDestinationHistory[vehicle].append(vehicleCapacity)
                self.vehicleDestinationHistory[vehicle].append(sumVehicleTravelDistance)
                vehicleCapacity = self.capacity

                vehicle += 1
                sumVehicleTravelDistance = 0
                self.vehicleDestinationHistory[vehicle] = []
                self.vehicleDestinationHistory[vehicle].append(0) 

    def showResults(self):
        totalDistanceTraveledByVehicles = 0
        totalClientsVisited = 1
        for vehicle in self.vehicleDestinationHistory:
            print("Vehicle Number", vehicle)
            print("Clients Visited", self.vehicleDestinationHistory[vehicle][:-2])
            print("Demand delivered by this vehicle", self.capacity - self.vehicleDestinationHistory[vehicle][-2])
            print("Traveled Distance", self.vehicleDestinationHistory[vehicle][-1], '\n')
            totalDistanceTraveledByVehicles += self.vehicleDestinationHistory[vehicle][-1]
            totalClientsVisited += (len(self.vehicleDestinationHistory[vehicle][:-2]) - 2)           
        print("Total Traveled Distance counting every vehicle: " + str(totalDistanceTraveledByVehicles))
        print("Number of Clients Visited: " + str(totalClientsVisited))

    def debugValues(self):
        print(self.vehicleDestinationHistory)
        #print(self.filename)
        #print(self.dimension)
        #print(self.capacity)
        #print(self.demand)
        #print(self.matrix)
        
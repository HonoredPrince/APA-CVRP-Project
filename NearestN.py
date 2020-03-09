# -*- coding: utf-8 -*-
from readDataFromFile import readFiles
import collections
from random import randrange

class NearestNeighbour:
    def __init__(self, instance):
        #Store all the data in the object constructor via calls in a readFiles object functions
        self.filename = str(instance)
        loader = readFiles(self.filename)
        self.demand = loader.get_stopPoints()
        self.matrix = loader.get_costMatrix()
        self.capacity = int(loader.get_capacity())
        self.dimension = int(loader.get_dimension())
        #This dictionary will map all vehicles destination history, e.g: {0: [0, 3, 4, 0]} --> Vehicle Number 0: Starts at 0, visited 3 and 4 and returned
        self.vehicleDestinationHistory = {}

        #Pass the string type values to int, had to change because it was conflicting the results
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = int(self.matrix[i][j])
        for key in self.demand:
            self.demand[key] = int(self.demand[key])

    def nearestNeighbourFunction(self):
        #Set variables and inital values for them
        currentClient = 0 #The first client to visit is the deposit itself, this is just to get first the 0 distance value for comparison
        clientsDemandSize = len(self.demand) #Number of clients to visit
        visitedClientsHistory = [0]

        #First vehicle starts
        vehicle = 0
        self.vehicleDestinationHistory[vehicle] = [0]
        sumVehicleTravelDistance = 0
        vehicleCapacity = self.capacity
        
        numberOfVertexToCompare = len(self.matrix[currentClient])
        
        #This while is going to run until all clients are visited 
        while len(visitedClientsHistory) < clientsDemandSize:
            #In the first iteration for every vehicle we only compare deposit location to itself
            #So in order to the 0 distance be accpeted in the if statement, use any fictional value
            #for the distance between Deposit(0) and Deposit(0)
            minDistanceCalculated = 777 
            clientToVisit = currentClient
            vehicleIsOkToProceed = False #Variable confirm if the vehicle is allowed to go to the next client or not

            #The 3 conditions for a visit to a certain client to be visited
            for client in range(numberOfVertexToCompare):
                if client not in visitedClientsHistory:
                    if(minDistanceCalculated > self.matrix[currentClient][client]):
                        if(vehicleCapacity - self.demand[str(client)] >= 0):
                            vehicleIsOkToProceed = True
                            clientToVisit = client #Client to visit is the client on the iteration
                            minDistanceCalculated = self.matrix[currentClient][client]

            #Update and store the information of the last iteration
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
            #If not, vehicle is set to return to the deposit 
            else:
                self.vehicleDestinationHistory[vehicle].append(0)
                sumVehicleTravelDistance += self.matrix[clientToVisit][0]
                self.vehicleDestinationHistory[vehicle].append(vehicleCapacity)
                self.vehicleDestinationHistory[vehicle].append(sumVehicleTravelDistance)
                vehicleCapacity = self.capacity

                #Send another vehicle and update some variables to default values
                vehicle += 1
                currentClient = 0
                sumVehicleTravelDistance = 0
                self.vehicleDestinationHistory[vehicle] = []
                self.vehicleDestinationHistory[vehicle].append(0) 
    
    #Fully randomized function for processing a instance and giving solutions, pretty much the same structure of the previous function
    def fullyRandomizedSolution(self):
        #Set variables and inital values for them
        currentClient = 0 #The first client to visit is the deposit itself, this is just to get first the 0 distance value for comparison
        clientsDemandSize = len(self.demand) #Number of clients to visit
        visitedClientsHistory = [0]

        #First vehicle starts
        vehicle = 0
        self.vehicleDestinationHistory[vehicle] = [0]
        sumVehicleTravelDistance = 0
        vehicleCapacity = self.capacity

        #self.vehicleDestinationHistory[vehicle].append(0)
        
        while len(visitedClientsHistory) < clientsDemandSize:
            #In the first iteration for every vehicle we only compare deposit location to itself
            #So in order to the 0 distance be accpeted in the if statement, use any fictional value
            #for the distance between Deposit(0) and Deposit(0) 
            randomClientGenerated = 0
            while randomClientGenerated in visitedClientsHistory:
                randomClientGenerated = randrange(1, clientsDemandSize)
            clientToVisit = randomClientGenerated 
            vehicleIsOkToProceed = False #Variable confirm if the vehicle is allowed to go to the next client or not

            #The 3 conditions for a visit to a certain client to be visited
            if clientToVisit not in visitedClientsHistory:
                if(vehicleCapacity - self.demand[str(clientToVisit)] >= 0):
                    vehicleIsOkToProceed = True
                    minDistanceCalculated = self.matrix[currentClient][clientToVisit] #Calculate the distance between the
                    currentClient = clientToVisit #Client to visit is now the current client that the vehicle is on
                else:
                    clientToVisit = visitedClientsHistory[-1]
            #Update and store the information of the last iteration
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
    

                
            #If not, vehicle is set to return to the deposit 
            else:
                self.vehicleDestinationHistory[vehicle].append(0)
                sumVehicleTravelDistance += self.matrix[clientToVisit][0]
                self.vehicleDestinationHistory[vehicle].append(vehicleCapacity)
                self.vehicleDestinationHistory[vehicle].append(sumVehicleTravelDistance)
                vehicleCapacity = self.capacity


                #Send another vehicle and update some variables to default values
                vehicle += 1
                currentClient = 0
                sumVehicleTravelDistance = 0
                self.vehicleDestinationHistory[vehicle] = []
                self.vehicleDestinationHistory[vehicle].append(0)
                
    #Function for showing the results for a specific instance
    #Pretty much all data is stored on Vehicle Destination history variable, and the information is retrieved from there 
    def showResults(self):
        totalDistanceTraveledByVehicles = 0 #For accounting total traveled distance by one vehicle
        totalClientsVisited = 1 #By default every vehicle starts at 0(Deposit) and return at the end there, so this variable starts at 1
        for vehicle in self.vehicleDestinationHistory:
            print("Vehicle Number", vehicle)
            print("Clients Visited", self.vehicleDestinationHistory[vehicle][:-2])
            print("Demand delivered by this vehicle", self.capacity - self.vehicleDestinationHistory[vehicle][-2])
            print("Traveled Distance", self.vehicleDestinationHistory[vehicle][-1], '\n')
            totalDistanceTraveledByVehicles += self.vehicleDestinationHistory[vehicle][-1]
            totalClientsVisited += (len(self.vehicleDestinationHistory[vehicle][:-2]) - 2)           
        print("Total Traveled Distance counting every vehicle: " + str(totalDistanceTraveledByVehicles))
        print("Number of Clients Visited: " + str(totalClientsVisited))

    #Function only for debugging purposes, should only be used for development stage
    #Just remove the comment tag for the respective result you want to see at certain point of the code
    #And call it on the part of the code you want 

    def debugValues(self):
        print(self.vehicleDestinationHistory)
        print(self.filename)
        print(self.dimension)
        print(self.capacity)
        print(self.demand)
        print(self.matrix)

    #This store the results of a method selected, must be called right after the method and not after all the types of execution are finished
    def storeRoutes(self):
        listOfRoutes = []
        for vehicle in self.vehicleDestinationHistory:
            listOfRoutes.append(self.vehicleDestinationHistory[vehicle][:-2])
            #print('\n' + str(listOfRoutes[vehicle]))
        print('\n' + 'List of routes: ' + str(listOfRoutes))
        return listOfRoutes
    
    #This function receives a list of routes that and show the total distance of that routes
    def calculateCost(self, routesArray):
        routes = routesArray
        distanceTraveled = 0
        for i in range(len(routes)):
            #print('i: ' + str(i))
            for j in range(len(routes[i]) - 1):
                #print('j: ' + str(j))
                distanceTraveled += self.matrix[routes[i][j+1]][routes[i][j]]
        print('Total Traveled Distance for the passed routes: ' + str(distanceTraveled))


        
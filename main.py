# -*- coding: utf-8 -*-
from NearestN import NearestNeighbour
from string import whitespace as ws
import re

#Basic menu, displays every instance filename avaliable
def inputMenu():
    print('----Filename Options----' + 
        '\nP-n16-k8' + 
        '\nP-n19-k2' + 
        '\nP-n20-k2' + 
        '\nP-n23-k8' + 
        '\nP-n45-k5' + 
        '\nP-n50-k10' + 
        '\nP-n51-k10' +
        '\nP-n55-k7' +
        '\n------------------------'
    )
    #If using python2 the input() function has to be changed to raw_input()
    instanceFilename = raw_input('\nEnter the instance filename:')
    instanceFilename = re.sub("^\s+|\s+$", "", instanceFilename, flags=re.UNICODE)
    while len(instanceFilename) < 8 or len(instanceFilename) > 9:
        print('\nInvalid input, please enter a correct filename for a instance!')
        instanceFilename = input('\nEnter the instance filename:')
        instanceFilename.strip()
    return instanceFilename + '.txt'

#Recieves input from function, and is directly passed onto the Object conctructor parameter
instance = inputMenu()
NearestNOperation = NearestNeighbour(instance)

#Calling functions to run the application and show the results
print('\n####### Nearest Neighbour Execution Results #######\n')
NearestNOperation.nearestNeighbourFunction()
NearestNOperation.showResults()
routes = NearestNOperation.storeRoutes()
distanceTraveledByPassedRoutes = NearestNOperation.calculateCost(routes)
#distanceTraveledByPassedRoutes, demandDeliveredByPassedRoutes = NearestNOperation.calculateCost(routes)
print('\nTotal Traveled Distance for the passed routes: ' + str(distanceTraveledByPassedRoutes))
#print('\nTotal Demand delivered for the passed routes: ' + str(demandDeliveredByPassedRoutes))

print('\nStarting Neighbour Movements Optimization')

print('\n##Intra Swap##')
routesSwaped = NearestNOperation.intraSwap(routes)

# def test():
#     for i in range(len(routes)):
#         routeDemand = NearestNOperation.getRouteDemand(routes[i])
#         minDelivery = NearestNOperation.getRouteMinDelivery(routes[i])
#         maxDelivery = NearestNOperation.getRouteMaxDelivery(routes[i])
#         print(routeDemand)
#         print(minDelivery)
#         print(maxDelivery)
# test()

print('\n####### Fully Randomized Execution Results #######\n')
NearestNOperation.fullyRandomizedSolution() 
NearestNOperation.showResults()
routes = NearestNOperation.storeRoutes()
distanceTraveledByPassedRoutes = NearestNOperation.calculateCost(routes)
#distanceTraveledByPassedRoutes, demandDeliveredByPassedRoutes = NearestNOperation.calculateCost(routes)
print('\nTotal Traveled Distance for the passed routes: ' + str(distanceTraveledByPassedRoutes))
#print('\nTotal Demand delivered for the passed routes: ' + str(demandDeliveredByPassedRoutes))

print('\nStarting Neighbour Movements Optimization')

print('\n##Intra Swap##')
routesSwaped = NearestNOperation.intraSwap(routes)


#NearestNOperation.debugValues() #Just use this function when debugging



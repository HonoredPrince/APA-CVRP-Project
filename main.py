# -*- coding: utf-8 -*-
from assets import CVRP
from string import whitespace as ws
from copy import deepcopy
import re

#Basic menu, displays every instance filename avaliable
def inputMenu():
    print('\n\n----Filename Options----' + 
        '\nP-n16-k8' + 
        '\nP-n19-k2' + 
        '\nP-n20-k2' + 
        '\nP-n23-k8' + 
        '\nP-n45-k5' + 
        '\nP-n50-k10' + 
        '\nP-n51-k10' +
        '\nP-n55-k7' +
        '\nExit() --> 0' +
        '\n------------------------'
    )
    #If using python2 the input() function has to be changed to raw_input()
    instanceFilename = input('\nEnter the instance filename:')
    instanceFilename = re.sub("^\s+|\s+$", "", instanceFilename, flags=re.UNICODE)
    if instanceFilename == '0':
        return 0
    else:
        while len(instanceFilename) < 8 or len(instanceFilename) > 9:
            if instanceFilename == '0':
                return 0
            print('\nInvalid input, please enter a correct filename for a instance!')
            instanceFilename = input('\nEnter the instance filename:')
            instanceFilename.strip()
        return instanceFilename + '.txt'
    
    
    

def main():
    while(True):
        instance = inputMenu()
        if instance != 0:
            #Recieves input from function, and is directly passed onto the Object conctructor parameter
            instanceOfCVRP = CVRP(instance)

            #Calling functions to run the application and show the results
            print('\n####### Nearest Neighbour Execution Results #######\n')
            instanceOfCVRP.nearestNeighbourFunction()
            instanceOfCVRP.showResults()
            #instanceOfCVRP.debugValues() #Just use this function when debugging
            routesForNearestNeighbour = instanceOfCVRP.storeRoutes()
            print('\n ----Resume for the nearest neighbour solution----')
            distanceTraveledByPassedRoutes = instanceOfCVRP.calculateTravelCost(routesForNearestNeighbour)
            demandDeliveredByPassedRoutes = instanceOfCVRP.calculateDemandDelivered(routesForNearestNeighbour)

            print('\nTotal Traveled Distance for the passed routes: ' + str(distanceTraveledByPassedRoutes))
            print('Total Demand delivered for the passed routes: ' + str(demandDeliveredByPassedRoutes))


            print('\nStarting Neighbour Movements Optimization...')

            print('\n######Intra Swap######')
            routesForIntraSwap = deepcopy(routesForNearestNeighbour)
            routesSwaped = instanceOfCVRP.intraSwap(routesForIntraSwap)

            print('\n##Inter Swap##')
            routesForInterSwap = deepcopy(routesForNearestNeighbour)
            routesSwaped = instanceOfCVRP.interSwap(routesForInterSwap)


            #Another solution, but this time is with random results
            print('\n####### Fully Randomized Execution Results #######\n')
            instanceOfCVRP.fullyRandomizedSolution() 
            instanceOfCVRP.showResults()
            routesForFullyRandomizedSolution = instanceOfCVRP.storeRoutes()
            print('\n ----Resume for the fully randomized solution----')
            distanceTraveledByPassedRoutes = instanceOfCVRP.calculateTravelCost(routesForFullyRandomizedSolution)
            demandDeliveredByPassedRoutes = instanceOfCVRP.calculateDemandDelivered(routesForFullyRandomizedSolution)

            print('\nTotal Traveled Distance for the passed routes: ' + str(distanceTraveledByPassedRoutes))
            print('Total Demand delivered for the passed routes: ' + str(demandDeliveredByPassedRoutes))

            print('\nStarting Neighbour Movements Optimization...')

            print('\n##Intra Swap##')
            routesForIntraSwap = deepcopy(routesForFullyRandomizedSolution)
            routesSwaped = instanceOfCVRP.intraSwap(routesForIntraSwap)

            print('\n##Inter Swap##')
            routesForInterSwap = deepcopy(routesForFullyRandomizedSolution)
            routesSwaped = instanceOfCVRP.interSwap(routesForInterSwap)

        else:
            break

main()
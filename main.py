# -*- coding: utf-8 -*-
from NearestN import NearestNeighbour
from string import whitespace as ws
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
    instanceFilename = raw_input('\nEnter the instance filename:')
    instanceFilename = re.sub("^\s+|\s+$", "", instanceFilename, flags=re.UNICODE)
    if instanceFilename == '0':
        return 0
    else:
        while len(instanceFilename) < 8 or len(instanceFilename) > 9:
            print('\nInvalid input, please enter a correct filename for a instance!')
            instanceFilename = input('\nEnter the instance filename:')
            instanceFilename.strip()
        return instanceFilename + '.txt'
    
    
    

def main():
    while(True):
        instance = inputMenu()
        if instance != 0:
            #Recieves input from function, and is directly passed onto the Object conctructor parameter
            NearestNOperation = NearestNeighbour(instance)

            #Calling functions to run the application and show the results
            print('\n####### Nearest Neighbour Execution Results #######\n')
            NearestNOperation.nearestNeighbourFunction()
            NearestNOperation.showResults()
            #NearestNOperation.debugValues() #Just use this function when debugging
            routes = NearestNOperation.storeRoutes()
            distanceTraveledByPassedRoutes = NearestNOperation.calculateTravelCost(routes)
            demandDeliveredByPassedRoutes = NearestNOperation.calculateDemandDelivered(routes)

            print('\nTotal Traveled Distance for the passed routes: ' + str(distanceTraveledByPassedRoutes))
            print('Total Demand delivered for the passed routes: ' + str(demandDeliveredByPassedRoutes))


            print('\nStarting Neighbour Movements Optimization...')

            print('\n######Intra Swap######')
            routesSwaped = NearestNOperation.intraSwap(routes)


            #Another solution, but this time is with random results
            print('\n####### Fully Randomized Execution Results #######\n')
            NearestNOperation.fullyRandomizedSolution() 
            NearestNOperation.showResults()
            routes = NearestNOperation.storeRoutes()
            distanceTraveledByPassedRoutes = NearestNOperation.calculateTravelCost(routes)
            demandDeliveredByPassedRoutes = NearestNOperation.calculateDemandDelivered(routes)

            print('\nTotal Traveled Distance for the passed routes: ' + str(distanceTraveledByPassedRoutes))
            print('Total Demand delivered for the passed routes: ' + str(demandDeliveredByPassedRoutes))

            print('\nStarting Neighbour Movements Optimization...')

            print('\n##Intra Swap##')
            routesSwaped = NearestNOperation.intraSwap(routes)
        else:
            break

main()
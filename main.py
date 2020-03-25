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

            #This section is for the execution using the nearest neighbour method to get a solution, after that execution the solution is passed for the optimization algorithms and the results are printed
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
            
            #Pass the solution to the optimization algorithms for the Nearest Neighbour execution
            print('\nStarting Neighbour Movements Optimization...')

            print('\n######Intra Swap######')
            routesForIntraSwap = deepcopy(routesForNearestNeighbour)
            routesIntraSwaped, costRoutesIntraSwaped = instanceOfCVRP.intraSwap(routesForIntraSwap)
            if routesIntraSwaped != [] and costRoutesIntraSwaped != 0:
                print('Best alternative route found by Intra swap algorithm: ' + str(routesIntraSwaped))
                print('Cost after optimization with Intra Swap: ' + str(costRoutesIntraSwaped))
            else:
                print('Intra Swap didn\'t optimzed any instance of routes at all!')

            print('\n##Inter Swap##')
            routesForInterSwap = deepcopy(routesForNearestNeighbour)
            routesInterSwaped, costRoutesInterSwaped = instanceOfCVRP.interSwap(routesForInterSwap)
            if routesInterSwaped != [] and costRoutesInterSwaped != 0:
                print('Best alternative route found by Inter swap algorithm: ' + str(routesInterSwaped))
                print('Cost after optimization with Inter Swap: ' + str(costRoutesInterSwaped))
            else:
                print('Inter Swap didn\'t optimzed any instance of routes at all!')

            print('\n##Reinsertion##')
            routesForReinsertion = deepcopy(routesForNearestNeighbour)
            routesReinserted, costRoutesReinserted = instanceOfCVRP.reinsertion(routesForReinsertion)
            if routesReinserted != [] and costRoutesReinserted != 0:
                print('Best alternative route found by Reinsertion algorithm: ' + str(routesReinserted))
                print('Cost after optimization with Reinsertion: ' + str(costRoutesReinserted))
            else:
                print('Reinsertion didn\'t optimzed any instance of routes at all!')

            print('\n##VND##')
            routesForVND = deepcopy(routesForNearestNeighbour)
            instanceOfCVRP.variableNeighborhoodDescent(routesForVND)


            #Another solution, but this time is with random results
            print('\n####### Fully Randomized Execution Results #######\n')
            instanceOfCVRP.fullyRandomizedSolution() 
            instanceOfCVRP.showResults()
            #instanceOfCVRP.debugValues() #Just use this function when debugging
            routesForFullyRandomizedSolution = instanceOfCVRP.storeRoutes()
            print('\n ----Resume for the fully randomized solution----')
            distanceTraveledByPassedRoutes = instanceOfCVRP.calculateTravelCost(routesForFullyRandomizedSolution)
            demandDeliveredByPassedRoutes = instanceOfCVRP.calculateDemandDelivered(routesForFullyRandomizedSolution)

            print('\nTotal Traveled Distance for the passed routes: ' + str(distanceTraveledByPassedRoutes))
            print('Total Demand delivered for the passed routes: ' + str(demandDeliveredByPassedRoutes))

            #Optimization of the fully random solution
            print('\nStarting Neighbour Movements Optimization...')

            print('\n##Intra Swap##')
            routesForIntraSwap = deepcopy(routesForFullyRandomizedSolution)
            routesIntraSwaped, costRoutesIntraSwaped = instanceOfCVRP.intraSwap(routesForIntraSwap)
            if routesIntraSwaped != [] and costRoutesIntraSwaped != 0:
                print('Best alternative route found by Intra swap algorithm: ' + str(routesIntraSwaped))
                print('Cost after optimization with Intra Swap: ' + str(costRoutesIntraSwaped))
            else:
                print('Intra Swap didn\'t optimzed any instance of routes at all!')

            print('\n##Inter Swap##')
            routesForInterSwap = deepcopy(routesForFullyRandomizedSolution)
            routesInterSwaped, costRoutesInterSwaped = instanceOfCVRP.interSwap(routesForInterSwap)
            if routesInterSwaped != [] and costRoutesInterSwaped != 0:
                print('Best alternative route found by Inter swap algorithm: ' + str(routesInterSwaped))
                print('Cost after optimization with Inter Swap: ' + str(costRoutesInterSwaped))
            else:
                print('Inter Swap didn\'t optimzed any instance of routes at all!')

            print('\n##Reinsertion##')
            routesForReinsertion = deepcopy(routesForFullyRandomizedSolution)
            routesReinserted, costRoutesReinserted = instanceOfCVRP.reinsertion(routesForReinsertion)
            if routesReinserted != [] and costRoutesReinserted != 0:
                print('Best alternative route found by Reinsertion algorithm: ' + str(routesReinserted))
                print('Cost after optimization with Reinsertion: ' + str(costRoutesReinserted))
            else:
                print('Reinsertion didn\'t optimzed any instance of routes at all!')

            print('\n##VND##')
            routesForVND = deepcopy(routesForFullyRandomizedSolution)
            vndSolution, costVND = instanceOfCVRP.variableNeighborhoodDescent(routesForVND)
            if vndSolution != [] and costVND != 0:
                print('Best alternative route found by VND algorithm: ' + str(vndSolution))
                print('Cost after optimization with VND: ' + str(costVND))
            else:
                print('VND didn\'t optimzed any instance of routes at all!')
        else:
            break

main()
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
    instanceFilename = input('\nEnter the instance filename:')
    instanceFilename = re.sub("^\s+|\s+$", "", instanceFilename, flags=re.UNICODE)
    while len(instanceFilename) < 8 or len(instanceFilename) > 9:
        print('\nInvalid input, please enter a correct filename for a instance!')
        instanceFilename = input('\nEnter the instance filename:')
        instanceFilename.strip()
    return instanceFilename + '.txt'

#Recieves input from function, and is directly passed onto the Object conctructor parameter
instance = inputMenu()
NearestNOperation = NearestNeighbour(instance)

#Calling functions to run the application
NearestNOperation.nearestNeighbourFunction()
NearestNOperation.showResults()

#NearestNOperation.debugValues() #Just use this function when debugging


from NearestN import NearestNeighbour
#from string import whitespace as ws
import re
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
    instanceFilename = input('\nEnter the instance filename:')
    instanceFilename = re.sub("^\s+|\s+$", "", instanceFilename, flags=re.UNICODE)
    while len(instanceFilename) != 8:
        print('\nInvalid input, please enter a correct filename for a instance!')
        instanceFilename = input('\nEnter the instance filename:')
        instanceFilename.strip()
    return instanceFilename + '.txt'

instance = inputMenu()
NearestNOperation = NearestNeighbour(instance)

NearestNOperation.nearestNeighbourFunction()
NearestNOperation.debugValues()
NearestNOperation.showResults()

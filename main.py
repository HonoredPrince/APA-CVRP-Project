from NearestN import NearestNeighbour

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
    while len(instanceFilename) != 8:
        print('\nInvalid input, please enter a correct filename for a instance!')
        instanceFilename = input('\nEnter the instance filename:')
    return instanceFilename + '.txt'

instance = inputMenu()
NearestNOperation = NearestNeighbour(instance)

NearestNOperation.nearestNedFlanders()
NearestNOperation.debugValues()
NearestNOperation.showResults()

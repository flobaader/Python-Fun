#Returns an 3D Array which contains all the candidates of the given Sudoku in z-Axis

def getCandiates(Sudoku):
    
    #List of Candidates
    Cands = [[[]]]
        
    #Adds the numbers 1 - 9 to the array
    Numbers = [i for i in range(1,10)]

    #Copy the values
    for x in range(0,9):
        for y in range(0,9):
            Cands[x][y][0] = Sudoku[x][y]

    #Go trough all numbers
    for x in range(0,9):
        for y in range(0,9):

            candidates = []

            #Check horizontal numbers
            candidates = deleteSameNumbers(Numbers, Sudoku[x])

            #Check vertical Numbers
            candidates2 = deleteSameNumbers(Numbers, Sudoku[][y]) 

def deleteSameNumbers(array1, array2):
    result = []
    for x1 in range(0, len(array1)):
        found = False
        for x2 in range(0, len(array2)):
            if(array1[x1] == array2[x2]):
                found = True
        if !found:
            result.append(x1)
    return result

def onlyKeepSameNumbers(array1, array2):
    result = []
    for x1 in range(0, len(array1)):
        found = False
        for x2 in range(0, len(array2)):
            if(array1[x1] == array2[x2]):
                found = True
        if found:
            result.append(x1)
    return result        
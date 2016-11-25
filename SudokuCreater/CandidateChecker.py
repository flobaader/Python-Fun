#Returns an 3D Array which contains all the candidates of the given Sudoku in z-Axis

import ArrayTools


def getCandidates(Sudoku):
    
    #List of Candidates
    Cands = ArrayTools.nullBased3DArray(9)
                
    #Adds the numbers 1 - 9 to the array
    Numbers = [i for i in range(1,10)]

    #Copy the values
    #for x in range(0,9):
    #    for y in range(0,9):
    #        Cands[x[y[0]] = Sudoku[x[y]]

    #Go trough all numbers
    for x in range(0,9):
        for y in range(0,9):

            candidates = []

            #Check horizontal numbers
            candidates = ArrayTools.deleteSameNumbers(Numbers, Sudoku[x])

            #Check vertical Numbers
            candidates2 = ArrayTools.deleteSameNumbers(Numbers, ArrayTools.getColumn(Sudoku, x))      
            candidates = ArrayTools.onlyKeepSameNumbers(candidates, candidates2)

            #Check sqaure Numbers
            candidates3 = ArrayTools.deleteSameNumbers(Numbers, ArrayTools.getSquare(Sudoku, x, y))
            candidates = ArrayTools.onlyKeepSameNumbers(candidates, candidates3)

            Cands[x][y].extend(candidates)              
    return Cands
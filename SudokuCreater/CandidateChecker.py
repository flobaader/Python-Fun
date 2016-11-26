import ArrayTools

def getCandidates(Sudoku, posX, posY):
    """
    Returns all possible candidates for the given position in the given Sudoku
    If a value == 0, it is seen as empty
    """
    
    #List of Candidates
    candidates = []
                
    #Adds the numbers 1 - 9 to the array
    Numbers = [i for i in range(1,10)]

    #Check vertical numbers
    candidates = ArrayTools.substractArray(Numbers, Sudoku[posX])

    #Check horizontal Numbers
    candidatesVert = ArrayTools.substractArray(Numbers, ArrayTools.getRow(Sudoku, posX))      
    candidates = ArrayTools.onlyKeepSameNumbers(candidates, candidatesVert)

    #Check sqaure Numbers
    candidatesSqr = ArrayTools.substractArray(Numbers, ArrayTools.getSquare(Sudoku, posX, posY))
    candidates = ArrayTools.onlyKeepSameNumbers(candidates, candidatesSqr)
       
    return candidates;
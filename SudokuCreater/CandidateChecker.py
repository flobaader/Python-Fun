import ArrayTools

def getCandidates(Sudoku, posX, posY):
    
    #List of Candidates
    candidates = []
                
    #Adds the numbers 1 - 9 to the array
    Numbers = [i for i in range(1,10)]

    #Check horizontal numbers
    candidates = ArrayTools.substractArray(Numbers, Sudoku[posX])

    #Check vertical Numbers
    candidatesVert = ArrayTools.substractArray(Numbers, ArrayTools.getRow(Sudoku, posX))      
    candidates = ArrayTools.onlyKeepSameNumbers(candidates, candidatesVert)

    #Check sqaure Numbers
    candidatesSqr = ArrayTools.substractArray(Numbers, ArrayTools.getSquare(Sudoku, posX, posY))
    candidates = ArrayTools.onlyKeepSameNumbers(candidates, candidatesSqr)
            
    return candidates;
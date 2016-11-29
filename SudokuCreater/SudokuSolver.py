import sys
import ArrayTools
import CandidateChecker

def solveSudoku(Sudoku):
    """
    Solves the given Sudoku, if there is a unique solution

    Returns the solved sudoku
    """

    while True:
        lowest_Candidates = 10
        lowest_posX  = 0
        lowestposY = 0
        solved = True

        Candidates = ArrayTools.nullBased3DArray(9)
        
        #Get candidates for all fields
        for x in range (0,9):
            for y in range (0,9):
                cands = CandidateChecker.getCandidates(Sudoku, x, y)
                Candidates[x][y] = cands
                                
                #Checks if the current field has the minimum numbers of candidates
                curCandCount = len(cands)
                #print(curCandCount)
                if(curCandCount > 0 & curCandCount < lowest_Candidates):
                    lowest_Candidates = curCandCount
                    lowest_posX = x
                    lowestposY = y
                
                #If there is any field which is not filled, the sudoku is not solved
                if(Sudoku[x][y] == 0):
                    solved = False

        #Check if the sudoku is already solved
        if (solved == True):
            print("Sudoku was succesfully solved!")
            return Sudoku

        print(lowest_Candidates)
        #Checks if the Sudoku is solvable
        if(lowest_Candidates == 1):
            solution = Candidates[lowest_posX][lowestposY][0]
            Sudoku[lowest_posX][lowestposY] = solution
            print("Got number " + solution + " as right number for (" + lowest_posX + "/" + lowestposY + ")")
            continue
        else:
            print("Sudoko is not solvable!")
            sys.exit(-1)

if __name__ == "__main__":

    import SudokuIOConverter

    Sudoku = SudokuIOConverter.getSudokoFromInput()

    print(solveSudoku(Sudoku))        
            
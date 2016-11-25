import RandomGenerator
import CandidateChecker
import ArrayTools

#NOTE: evtl. x  / y vertauscht
#NOTE: Doc Kommentare einbinden

def GenerateSudoku():
    Sudoku = ArrayTools.nullBased2DArray(9)

    succesfull = 0
    countTries = 0

    while succesfull < 1:
        for x in range (0,9):
            for y in range(0,9):
                cands = CandidateChecker.getCandidates(Sudoku, x, y)

                #Check if there are no more candidates
                if(len(cands) == 0):
                    succesfull = -1
                    print("Sudoku Generation Failed :" + str(countTries))
                    countTries = countTries + 1
                    break
                else:
                    Sudoku[x][y] = RandomGenerator.GenerateRandom(cands)

                #Check if succesfull
                if((x == 8) & (y == 8)):
                    succesfull = 1
            if(succesfull == -1):
                break
    return Sudoku

if __name__ == "__main__":
    print(GenerateSudoku())
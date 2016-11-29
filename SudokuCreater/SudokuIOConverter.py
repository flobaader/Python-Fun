import ArrayTools
import sys

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def getSudokoFromInput():
    Sudoku = ArrayTools.nullBased2DArray(9)

    for y in range (0,9):
        eingabe = input("Bitte geben Sie die " + str(y + 1) + ". Zeile ein: \n")

        #Check for valid input
        if(len(eingabe) != 9 | is_number(eingabe) == False):
            print("Could not convert the given string to a Sudoko!")
            sys.exit(-1)  
        else:
            for x in range(0,9):
                number =  int(eingabe[x])
                Sudoku[x][y] = number
    return Sudoku

def printSudoku(Sudoku):
    output = ""
    for y in range(0,9):
        for x in range(0,9):
            output = output + str(Sudoku[x][y])
        output = output + "\n"
    print(output)
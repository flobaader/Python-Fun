
#Returns an array which only contains numbers, which are not in both arrays
def deleteSameNumbers(array1, array2):
    result = []
    for x1 in range(0, len(array1)):
        found = False
        for x2 in range(0, len(array2)):
            if(array1[x1] == array2[x2]):
                found = True
        if found == False:
            result.append(x1)
    return result

#Returns an array with all numbers, which are represented in both arrays
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

#Returns the column of the given 2D array at the given index
def getColumn(array, index):
    column = []
    for i in range(0,9):
        column.append(array[i][index])
    return column

def getSquare(Sudoku, posX, posY):
    Cands = []
    SqX = int(posX / 3)
    SqY = int(posY / 3)

    for x in range (SqX * 3, SqX * 3 + 3):
        for y in range (SqY * 3, SqY * 3 + 3):
            Cands.append(Sudoku[x][y])
    return Cands
    
def nullBased2DArray(length):
    array = [[]]
    array[0] = nullBasedArray(length)  
    for x in range(0, length - 1):
            array.append(nullBasedArray(length))
    return array


def nullBasedArray(length):
    array = []
    for i in range (0,length):
        array.append(0)
    return array

def nullBased3DArray(length):
    array = [[[]]]
    array[0] = nullBased2DArray(length)
    for x in range (0,length-1):
        temp = nullBased2DArray(length)
        array.append(temp)
    return array;            
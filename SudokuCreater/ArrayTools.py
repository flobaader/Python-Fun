import math

#Returns an array which only contains numbers, which are not in both arrays
def substractArray(array1, array2):
    """
    Substracts array2 of array1.
    That means, that every number in array1, which is also present in array2 is deleted
    """
    result = array1.copy()

    for i in range(0,len(array2)):
        while (result.count(array2[i]) > 0):
            result.remove(array2[i])
    return result
  

#Returns an array with all numbers, which are represented in both arrays
def onlyKeepSameNumbers(array1, array2):
    result = []
    for x1 in range(0, len(array1)):
        found = False
        for x2 in range(0, len(array2)):
            if(array1[x1] == array2[x2] & array1[x1] != 0):
                found = True
        if found:
            result.append(array1[x1])
    return result

#Returns the column of the given 2D array at the given index
def getRow(array, index):
    column = []
    for i in range(0,9):
        column.append(array[index][i])
    return column

def getSquare(Sudoku, posX, posY):
    numbers = []
    SqX = math.floor(posX / 3)
    SqY = math.floor(posY / 3)

    for x in range (SqX * 3, SqX * 3 + 3):
        for y in range (SqY * 3, SqY * 3 + 3):
            if(Sudoku[x][y] != 0):
                numbers.append(Sudoku[x][y])
    return numbers
    
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
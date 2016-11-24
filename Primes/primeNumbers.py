import sys

def isPrime(number):
    i = 2
    isPrime = True
    while i < (number / 2):
        i =  i + 1
        if(number%i == 0):
            isPrime = False
            break
    return isPrime

def getPrimeNumbersTo(maxI):
    i = 2
    primzahlen = []
    primzahlen.append(2)

    while True:
        i = i+1 
        istPrimzahl = True
        arrayInd = 0
        
        Teiler = primzahlen[arrayInd]
        while Teiler < (i/2):
            if(i%Teiler == 0):
                istPrimzahl = False
            arrayInd = arrayInd + 1
            Teiler = primzahlen[arrayInd]

        if(istPrimzahl):
            primzahlen.append(i)
        if(i == maxI):
            print("Done finding PrimeNumbers!")
            return primzahlen
        
if __name__ == "__main__":
    argCounter = 1
    if(len(sys.argv) != 3):
        print("Wrong use of Arguments!")
        print("Use -R for Range, -S for Single and then the number")
        print("Example: -R 200")
        sys.exit(2)
    else:
        number = int(sys.argv[2])
        if(sys.argv[1] == "-S"):
            print(isPrime(number))
            sys.exit(1)
        else:
            if(sys.argv[1] == "-R"):
                print(getPrimeNumbersTo(number))
                sys.exit(1)
            else:
                print("Wrong Use of Argument!")
                sys.exit(1)
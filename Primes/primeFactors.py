#Primfaktorzerlegung
import primeNumbers
import sys
from optparse import OptionParser
       

#gets all prime numbers smaller than the given Value 
#divides new number through all already found prime numbers
def getPrimeFactors(number):
    primes = primeNumbers.getPrimeNumbersTo(number)
    factors = []
    i = 0
    while (i < len(primes)):
        factor = primes[i]
        while (number% factor == 0):
            factors.append(factor)
            number = number / factor
        i = i + 1

        if(number == 1):
            break
    return factors

#Main
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-n", "--number", dest="number", help="Specify the number, that should be factored.", metavar="NUMBER")
    (options, args) = parser.parse_args()
    i = int(options.number)
    print(getPrimeFactors(i))


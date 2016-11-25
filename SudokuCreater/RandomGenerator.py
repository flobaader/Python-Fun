import random

def GenerateRandom(arrayCandidates):
    randomIndex = random.randint(0, len(arrayCandidates)-1)
    print(randomIndex)
    return arrayCandidates[randomIndex]    
import random

def GenerateRandom(arrayCandidates):
    randomIndex = random.randint(0, len(arrayCandidates)-1)

    return arrayCandidates[randomIndex]    
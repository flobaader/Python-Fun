import random

def GenerateRandom(arrayCandidates):
    """
    Returns a random value of the given values in the array
    """
    randomIndex = random.randint(0, len(arrayCandidates)-1)
    return arrayCandidates[randomIndex]    
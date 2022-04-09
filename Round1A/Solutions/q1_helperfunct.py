import string
import random

def functiontest(inputstring):
    possibles = []
    inputlength = len(inputstring)
    for x in range(0,inputlength):
        tooadd = ''
        binaryswitch = "{0:b}".format(x).ljust(inputlength,'0')
        for index_a, letter in enumerate(inputstring):
            if binaryswitch[index_a] == '1':
                tooadd += letter
            tooadd += letter
        possibles.append(tooadd)
    possibles.sort()
    return possibles[0]
        
def randomstring(x):
    returnstring = ''
    for x in range(0,x):
        returnstring += (random.choice(string.ascii_letters.upper()))
    return returnstring

stringtofind  = randomstring(6)
print(stringtofind)
print(functiontest(stringtofind))

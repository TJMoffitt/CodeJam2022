##import math
##import sys
##import itertools
import string
import random

def functiontest(inputstring):
    possibles = []
    inputlength = len(inputstring)
    for x in range(0,inputlength):
        tooadd = ''
        binaryswitch = "{0:b}".format(x).ljust('0',inputlength)
        for index_a, letter in enumerate(inputstring):
            if binaryswitch[index_a] == '1':
                tooadd += letter
            tooadd += letter
        possibles.append(tooadd)
    possibles.sort()
    return possibles[0]

def exists_greater(letter,string):
    currentletter = letter
    string = letter + string

    for index in range(0,len(string)):
        try:
            if string[index] < string[index+1]:
                return True
            if string[index] == string[index+1]:
                pass
            else:
                break
        except:
            return False
##        if letter <= string[0] and string[index:].replace(letter,'') != '':
##            return True
    return False
    for other_letter in string:
        if currentletter < other_letter:
            return True
        currentletter == other_letter
##        if not flipped and letter != other_letter:
##            flipped == True
##        if ord(other_letter) > ord(letter) and flipped:
##            return True
##    if flipped == False:
##        return True
    return False

def main_function(inp_one,inp_two = 0, inp_three = 0, inp_four = 0):
    newstring = ''
    letterindex = -1
    while True:
        letterindex += 1
        newstring += inp_one[letterindex]
        if letterindex == len(inp_one) -1:
            return newstring
        letter = inp_one[letterindex]
        if ord(letter) <= ord(inp_one[letterindex+1]) and exists_greater(letter,inp_one[letterindex+1:]):
            newstring += letter

##    for letter in inp_one:
##        newstring += letter
##        if letterindex == len(inp_one)-1:
##            return newstring
##
##        if ord(letter) <= ord(inp_one[letterindex+1]) and exists_greater(letter,inp_one[letterindex+1:]) and :
##            newstring += letter
##        
##    pass


##def functiontest(inputstring):
##    possibles = []
##    inputlength = len(inputstring)
##    for x in range(0,2**inputlength):
##        tooadd = ''
##        binaryswitch = "{0:b}".format(x).ljust(inputlength,'0')
##        for index_a, letter in enumerate(inputstring):
##            if binaryswitch[index_a] == '1':
##                tooadd += letter
##            tooadd += letter
##        possibles.append(tooadd)
##    possibles.sort()
##    return possibles[0]
##        
##def randomstring(x):
##    returnstring = ''
##    for x in range(0,x):
##        returnstring += (random.choice(string.ascii_letters.upper()))
##    return returnstring
##while True:
##    stringtofind  = randomstring(6)
##    functiona = main_function(stringtofind)
##    functionb = functiontest(stringtofind)
##    if functiona != functionb:
##        if functiona > functionb:
##            print(stringtofind)
##            print("should be smaller: " + main_function(stringtofind))
##            print("shoudl be larger:  " + functiontest(stringtofind))
##            break
##        


def main():
    nocases = int(input())
    for x in range(1,nocases+1):
        inp_one = input().upper()
##        inp_two = [int(x) for x in input().split(' ')]
##        inp_two = int(input())        
##        inp_two = {}
##        for xtwo in range(0,inp_one):
##            inp_two_key, inp_two_num = input().split(' ')
##            inp_two[int(inp_two_key)] = int(inp_two_num)
##            if int(inp_two_key) in inp_two:
##                inp_two[int(inp_two_key)] += int(inp_two_num)
##            else:
##               inp_two[int(inp_two_key)] = int(inp_two_num) 
                    
##        inp_two = []
##        for xtwo in range(0,inp_one):
##            inp_two_key, inp_two_num = input().split(' ')
##            inp_two.append([int(inp_two_key),int(inp_two_num)]) 

        print(f'Case #{x}: ' + str(main_function(inp_one)))
    

main()
##
####val = [('first', 3, 9), ('second', 4, 6), ('third', 2, 3)]
####val.sort(key = lambda x: x[2], reverse=False)
####print(val)

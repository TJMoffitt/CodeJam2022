import math
import sys

def main_function(inp_one,inp_two = 0, inp_three = 0, inp_four = 0):
    print(inp_one)
    print(inp_two)
    print(inp_three)
    print(inp_four)
    pass


def main():
    nocases = int(input())
    for x in range(1,nocases+1):
        inp_one = int(input())
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
                    
        inp_two = []
        for xtwo in range(0,inp_one):
            inp_two_key, inp_two_num = input().split(' ')
            inp_two.append([int(inp_two_key),int(inp_two_num)]) 

        print(f'Case #{x}: ' + str(main_function(inp_one,inp_two)))
    

main()

##val = [('first', 3, 9), ('second', 4, 6), ('third', 2, 3)]
##val.sort(key = lambda x: x[2], reverse=False)
##print(val)

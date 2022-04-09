import math
import sys
import itertools
import bisect

def main_function(inp_one,inp_two = 0, inp_three = 0, inp_four = 0):
    array = []
    for x in range(0,inp_one):
        if 2**x < 10**9:
            array.append(2**x)
        else:
            array.append(x*3)
    if sum(array) % 2 != 0:
        array[-1] = 2
    array.sort()
    array[0] = 1
    return array

#print(main_function(50))


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
##                    
##        inp_two = []
##        for xtwo in range(0,inp_one):
##            inp_two_key, inp_two_num = input().split(' ')
##            inp_two.append([int(inp_two_key),int(inp_two_num)]) 
        firstarray = main_function(inp_one)
        print(str(firstarray)[1:-1].replace(",",""))
        secondarray = [int(x) for x in input().split(' ')]
        firstarray.sort()
        secondarray.sort()
        totaltofind = sum(secondarray) + sum(firstarray)
        totaltofind = int(totaltofind/2)
        #print('test')
        foundnumbers = []
        totalleft = totaltofind
        while totalleft > 0:
            #print(totalleft)
            if totalleft >= 10**9 and len(secondarray) != 0:
                foundnumbers.append(secondarray[-1])
                totalleft -= secondarray[-1]
                secondarray = secondarray[:-1]
            else:
                index = bisect.bisect(firstarray,totalleft)
                #print(index)
                totalleft -= firstarray[index-1]
                foundnumbers.append(firstarray[index-1])
##                indicies = [v for i,v in enumerate(firstarray) if v != max(firstarray)]
##                totalleft -= max(indicies)
##                for element_index, element in enumerate(firstarray):
##                    try:
##                        if element <= totalleft and firstarray[element_index+1] > totalleft: #or element_index == len(firstarray)-1:
##                            if element_index != 0:
##                                foundnumbers.append(element)
##                                totalleft -= element
##                                firstarray = firstarray[:element_index]
##                                break
##                    except:
##                        if element <= totalleft:
##                            if element_index != 0:
##                                foundnumbers.append(firstarray[element_index-1])
##                                totalleft -= firstarray[element_index-1]
##                                firstarray = firstarray[:-1]
##                                break
##                if totalleft != 0:
##                    foundnumbers.append(firstarray[-1])
##                    totalleft -= firstarray[-1]
##                    firstarray = firstarray[:-1]
            #print(totalleft)
        print(str(foundnumbers)[1:-1].replace(",",""))
    

main()
##
####val = [('first', 3, 9), ('second', 4, 6), ('third', 2, 3)]
####val.sort(key = lambda x: x[2], reverse=False)
####print(val)
##
##from collections import defaultdict
## 
### Function to find number of subarrays 
### with sum exactly equal to k.
##def findSubarraySum(arr, n, Sum):
##  
##    # Dictionary to store number of subarrays
##    # starting from index zero having 
##    # particular value of sum.
##    prevSum = defaultdict(lambda : 0)
##   
##    res = 0
##   
##    # Sum of elements so far.
##    currsum = 0
##   
##    for i in range(0, n): 
##   
##        # Add current element to sum so far.
##        currsum += arr[i]
##   
##        # If currsum is equal to desired sum,
##        # then a new subarray is found. So
##        # increase count of subarrays.
##        if currsum == Sum:
##            
##            res += 1        
##   
##        # currsum exceeds given sum by currsum  - sum.
##        # Find number of subarrays having 
##        # this sum and exclude those subarrays
##        # from currsum by increasing count by 
##        # same amount.
##        if (currsum - Sum) in prevSum:
##            res += prevSum[currsum - Sum]
##           
##        # Add currsum value to count of 
##        # different values of sum.
##        prevSum[currsum] += 1
##      
##    return res
##  
##if __name__ == "__main__":
## 
##    arr =  [10, 2, -2, -20, 10] 
##    Sum = -10
##    n = len(arr)
##    print(findSubarraySum(arr, n, Sum))

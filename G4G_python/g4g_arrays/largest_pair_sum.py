'''
Created on 07-Mar-2019

@author: shiva
'''
def findLargestSum(array):
    if(array[0]>array[1]):
        first=array[0]
        second=array[1]
    else:
        second=array[0]
        first=array[1]
            
    for i in array[2:]:
        if i>first:
            second=first
            first=i
        elif i>second:
            second=i
    return first+second
def findSmallestSum(array):
    if(array[0]<array[1]):
        first=array[0]
        second=array[1]
    else:
        second=array[0]
        first=array[1]
            
    for i in array[2:]:
        if i<first:
            second=first
            first=i
        elif i<second:
            second=i
    return first+second

a=[88,12, 34, 10, 6, 40,5,0]
print(findLargestSum(a))
print(findSmallestSum(a))

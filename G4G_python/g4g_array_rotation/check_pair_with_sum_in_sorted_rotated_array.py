'''
Created on 27-Feb-2019

@author: shiva
'''
def findPivot(array):
    if len(array)<1:
        return -1
    for i in range(len(array)-1):
        if(array[i]>array[i+1]):
            return i
    return len(array)

def hasPair(array,sum):
    n=len(array)
    l=findPivot(array)
    r=l+1
    while(l!=r):
        s=array[l]+array[r]
        if(s==sum):
            return 1
        elif(s>sum):
            l=(n+l-1)%n
        else:
            r=(r+1)%n
    return 0
        
a=[10,45,-8,1,4,6]
sum=5
res=hasPair(a, sum)
if res==1:
    print('has pair')
else:
    print('no pair')
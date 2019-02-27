'''
Created on 27-Feb-2019

@author: shiva
'''
def hasPair(array,sum):
    if(len(array)<1):
        return -1
    l=0;r=len(array)-1
    while(l<r):
        if(array[l]+array[r]==sum):
            return 1
        elif(array[l]+array[r]<sum):
            l=l+1
        else:
            r=r-1        
    return 0;
a=[-8,1,4,6,10,45]
sum=16
res=hasPair(a, sum)
if(res==1):
    print('has pair')
elif(res==0):
    print('no pair')
else:
    print('invalid array')

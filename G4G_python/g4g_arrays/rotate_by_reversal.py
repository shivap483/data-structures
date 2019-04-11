'''
Created on 16-Jan-2019

@author: shiva
'''
def reverse(ar, start,end):
    while(start<end):
        temp=ar[start]
        ar[start]=ar[end]
        ar[end]=temp
        start=start+1
        end=end-1
    return ar

def rotate(ar,rotateCount):
    ar=reverse(ar, 0, rotateCount-1)
    ar=reverse(ar, rotateCount, len(ar)-1)
    ar=reverse(ar, 0, len(ar)-1)
    return ar

ar=[1,2,3,4,5,6,7,8]
print(ar)
n=3
print(rotate(ar, n))
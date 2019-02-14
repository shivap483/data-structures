'''
Created on 23-Jan-2019

@author: shiva
'''
def binarySearch(arr, low, high, key):
    if(high<low):
        return -1;
    mid= int((high+low)/2)
    if(arr[mid]==key):
        return mid;
    if key>arr[mid]:
        return binarySearch(arr, mid+1, high, key);
    return binarySearch(arr, low, mid-1, key)

def findElement(ar, n):
    pivot= findPivot(ar,0, n)
    if pivot==-1:
        return binarySearch(ar, 0, len(ar), n)
    if n<ar[0]:
        return binarySearch(ar, pivot+1, len(ar), n)
    return binarySearch(ar, 0, pivot, n)
    return;
    
def findPivot(arr, low, high):
    if high<low:
        return -1
    if high==low:
        return low;
    
    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1]):
            return i;
        
    return -1;
    
       
    
    
ar=[5,6,7,1,2,3,4]
n=1
position=findElement(ar, n)
print('found at position: ',position)
        
        
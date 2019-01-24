'''
Created on 23-Jan-2019

@author: shiva
'''
def binary_search(ar,elementToSearch):
    if(len(ar)==0):
        print('false')
    mid=int(len(ar)/2)
    if(elementToSearch==ar[mid]):
        return mid+1
    elif(elementToSearch<ar[mid]):
        l=binary_search(ar[:mid], elementToSearch)
        return l   
    else:
        l=mid+binary_search(ar[mid+1:], elementToSearch)
        return l+1
    
def find_pivot(ar):
    i=0
    while(i<len(ar)-1):
        if(ar[i]>ar[i+1]):
            break
        i=i+1
    return i
def find_element(ar,elementToSearch):
    pivot=find_pivot(ar)
    left_array=ar[:pivot+1]
    if(pivot!=len(ar)):
        right_array=ar[pivot+1:]
    if(elementToSearch<left_array[0]):
        return len(left_array) + binary_search(right_array, elementToSearch)
    return binary_search(left_array, elementToSearch)
#     if(elementToSearch==ar[pivot]):
#         return pivot
#     if(elementToSearch<=ar[pivot]):
#         return binary_search(ar[:pivot], elementToSearch)
#     else:
#         return binary_search(ar[pivot:], elementToSearch)
        
ar=[5,6,7,1,2,3,4]
n=10
position=find_element(ar, n)
print('found at position: ',position)
        
        
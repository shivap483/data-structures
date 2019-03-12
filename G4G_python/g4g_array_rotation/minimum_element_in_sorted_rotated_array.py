def findMinElement(arr, low, high):
	if(high<low):
		return -1
		
	if(high==low):
		return arr[low]
		
	mid= int((high+low)/2)
	
	if(mid<high and arr[mid]>arr[mid+1]):
		return arr[mid+1]
		
	if(mid>low and arr[mid-1]>arr[mid]):
		return arr[mid]
	
	if(arr[high]>arr[mid]):
		return findMinElement(arr, low, mid-1)
		
	return findMinElement(arr, mid+1, high)
	
arr=[1, 2, 3, 4, 5, 6, 7]
n=len(arr)
high=n-1
low=0
print(findMinElement(arr, 0, n-1))
def countRotations(arr, low, high):
	mid= (high + low) / 2
	if(high<low):
		return 0
	
	if(high==low):
		return low
		
	if(mid<high and arr[mid]>arr[mid+1]):
		return mid+1
	
	if(mid>low and arr[mid-1]>arr[mid]):
		return mid
	
	if(arr[high]>arr[mid]):
		return countRotations(arr, low, mid-1)
			
	return countRotations(arr, mid+1, high)
		
arr=[15, 18, 2, 3, 6, 12]	
high=len(arr)-1
low=0
print(countRotations(arr, low, high))
	
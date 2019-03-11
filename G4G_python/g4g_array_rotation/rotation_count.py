def countRotations(arr,n):
	for i in range(n-1):
		if(arr[i]>arr[i+1]):
			return (i+1)%n
		return 0	
arr=[7, 9, 11, 12, 15]
n=len(arr)
print(countRotations(arr,n))
def findPivot(arr):
	pivot=arr[0]
	for i in arr:
		if(i>pivot):
			pivot=i
	return pivot
	
def findMaxSum(arr):
	pivot=findPivot(arr)
	n=len(arr)
	diff=n-1-pivot
	maxVal=0
	for i in range(n):
		maxVal=maxVal+((diff+i)%n)*arr[i]
	return maxVal
	
arr=[8, 3, 1, 2]
print(findMaxSum(arr))
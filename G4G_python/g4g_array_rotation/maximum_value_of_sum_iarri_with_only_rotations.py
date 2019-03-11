def arraySum(arr):
	aSum=0
	for i in arr:
		aSum=aSum+i;
	return aSum;

def findMaxSum(arr):
	arrSum=arraySum(arr);
	n=len(arr)
	curVal=0
	for i in range(n):
		curVal=curVal+i*arr[i];
	
	maxVal=curVal
	for i in range(1,n):
		curVal=arrSum-n*arr[n-i]+curVal
		if(curVal>maxVal):
			maxVal=curVal
	return maxVal

arr=[1,20,2,10]
print(findMaxSum(arr))
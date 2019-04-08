def arraySum(arr):
	aSum = 0
	curVal = 0;
	for i in range(len(arr)):
		curVal = curVal + i * arr[i];
		aSum = aSum + arr[i];
	return aSum, curVal;


def findMaxSum(arr):
	arrSum, curVal = arraySum(arr);
	n = len(arr)
	
	maxVal = curVal
	for i in range(1, n):
		curVal = arrSum - n * arr[n - i] + curVal
		if(curVal > maxVal):
			maxVal = curVal
	return maxVal


arr = [1, 20, 2, 10]
print(findMaxSum(arr))

def rotateLeft(arr,n,k):
	for i in range(k, n+k):
		print(arr[i%n], end=" ")
	print("")
		
arr=[1, 3, 5, 7, 9]
n=len(arr)

k=2
rotateLeft(arr,n,k)

k=3
rotateLeft(arr,n,k)

k=14
rotateLeft(arr,n,k)
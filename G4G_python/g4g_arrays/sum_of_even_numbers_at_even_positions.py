def getSum(arr,n):
    sum=0
    for i in range(n):
        if(i%2==0 and arr[i]%2==0):
            sum=sum+arr[i]
    return sum

arr = [5, 6, 12, 1, 18, 8]
print(getSum(arr,len(arr)))
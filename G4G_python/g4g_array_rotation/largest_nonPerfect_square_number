import math
def getMaxNonPerfectSquare(arr,n):
    temp=-1
    for i in range(n):
        if(checkNonperfectSquare(arr[i])and temp<arr[i]):
            temp=arr[i]
    return temp

def checkNonperfectSquare(x):
    root=int(math.sqrt(x))
    if (root*root==x):
        return False
    return True

arr = [16, 20, 25, 2, 3, 10]
print(getMaxNonPerfectSquare(arr,len(arr)))
def rotateRight(ar,d,n):
    for i in range(d):
        ar=rotateRightByOne(ar, n-1);
    return ar
def rotateRightByOne(ar,n):
    temp=ar[n]
    for i in range(n):
        ar[n-i]=ar[n-i-1]
    ar[0]=temp
    return ar

def rotateLeft(ar,d,n):
    for i in range(d):
        ar=rotateLeftByOne(ar,n-1)
    return ar

def rotateLeftByOne(ar,n):
    temp=ar[0]
    for i in range(n):
        ar[i]=ar[i+1]
    ar[n]=temp
    return ar


ar=[1,2,3,4,5,6]
print(ar)
print(rotateRight(ar, 3, len(ar)))
print(rotateLeft(ar, 5, len(ar)))
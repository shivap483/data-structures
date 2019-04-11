def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)
    
def rotate_by_juggling(ar,d,n):
    for i in range(gcd(d, n)):
        temp= ar[i]
        j=i
        while True:
            k=d-j
            if k<=0:
                k=k+d
            if k==d:
                break
            ar[j]=ar[k]
            j=k
        ar[j]=temp
    return ar

ar=[1,2,3,4,5,6]
print(ar)
print(rotate_by_juggling(ar, 4, len(ar)))

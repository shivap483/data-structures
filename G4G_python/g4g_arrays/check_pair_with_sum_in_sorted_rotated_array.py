'''
Created on 27-Feb-2019

@author: shiva
'''


def findPivot(array):
    n = len(array)
    if n < 1:
        return -1
    for i in range(n - 1):
        if(array[i] > array[i + 1]):
            return i
    return n - 1


def hasPair(array, sum):
    n = len(array)
    l = findPivot(array)
    r = (l + 1) % n
    count = 0
    while(l != r):
        s = array[l] + array[r]
        if(s == sum):
            count = count + 1            
            if r == (l + n - 1) % n:
                break
            l = (n + l - 1) % n
            r = (r + 1) % n
        elif(s > sum):
            l = (n + l - 1) % n
        else:
            r = (r + 1) % n
    return count

        
a = [ 10, 15, 18, 45, -8, 0, 1, 2, 3, 4, 5, 6, 7]
sum = 7
res = hasPair(a, sum)
if res >= 1:
    print(res)
else:
    print('no pair')

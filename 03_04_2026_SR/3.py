def maxelement(a):
    mx = float('-inf')
    index = 0
    for i in range(len(a)):
        if mx < a[i]:
            mx = a[i]
            index = i
    return mx, index

def leastelement(a):
    mx = float('inf')
    index = 0
    for i in range(len(a)):
        if mx > a[i]:
            mx = a[i]
            index = i
    return mx, index

from random import randrange
arr = []

n = int(input())
m = int(input())

for i in range(n):
    arr.append([])
for i in range(n):
    for j in range(m):
        arr[i].append(randrange(0, 100))

for i in range(n):
    mxn, mxi = maxelement(arr[i])
    lsn, lsi = leastelement(arr[i])
    var = arr[i][0]
    arr[i][0] = mxn; arr[i][mxi] = var
    var = arr[i][m-1]
    arr[i][m-1] = lsn; arr[i][lsi] = var

print(arr)

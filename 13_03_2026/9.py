from random import randrange
size = 5
arr = []
for i in range(size):
    vararr = []
    for j in range(size):
        vararr.append(randrange(-50, 51))
    arr.append(vararr)

mosum = 0
for i in range(size):
    for j in range(size):
        if arr[i][j] % 2 != 0 and arr[i][j] < 0:
            mosum += abs(arr[i][j])
print(mosum)
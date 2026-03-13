from random import randrange
size = int(input("Enter matrix size: "))
arr = []
for i in range(size):
    vararr = []
    for j in range(size):
        vararr.append(randrange(1, 100))
    arr.append(vararr)

for i in range(size):
    print(arr[i])

minsubdiag = arr[1][size - 1]
for i in range(1, size):
    for j in range(size - 1, i, -1):
        if arr[i][j] <= minsubdiag:
            minsubdiag = arr[i][j]
print(minsubdiag)
mult = 1
for i in range(size):
    if arr[size - 1][i] != 0:
        mult *= arr[size - 1][i]
print(mult)
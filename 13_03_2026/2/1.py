from random import randrange
arr = []
for i in range(20):
    arr.append(randrange(-10, 11))

print(arr)

for i in range(20):
    if arr[i] > 0:
        arr[i] = 1
    elif arr[i] < 0:
        arr[i] = -1

print(arr)
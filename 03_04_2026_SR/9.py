from random import randrange

def mularr(a, n):
    if n == 0:
        return 1
    return a[n - 1] * mularr(arr, n - 1)

arr = []

for i in range(10):
    arr.append(randrange(1, 10))

print(arr)

print(mularr(arr, len(arr)))

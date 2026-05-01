from random import randrange
arr = []
for i in range(10):
    arr.append(randrange(0, 101))
arr.sort(reverse=True)
print(arr)
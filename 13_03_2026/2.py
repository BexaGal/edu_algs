from random import randrange
arr = []
for i in range(10):
    vararr = []
    for j in range(10):
        vararr.append(randrange(1, 100))
    arr.append(vararr)

for i in range(10):
    print(arr[i])

maxline = arr[i]
for i in range(10):
    if sum(arr[i]) > sum(maxline):
        maxline = arr[i]
print("Maxline:")
print(maxline)
from random import randrange
size = int(input("Enter matrix size: "))
arr = []
for i in range(size):
    vararr = []
    for j in range(size):
        vararr.append(randrange(1, 100))
    arr.append(vararr)

for i in range(size):
    if i % 2 == 0:
        print(arr[i])
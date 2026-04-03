from random import randrange
arr = []
for i in range(2):
    vararr = []
    for j in range(3):
        vararr.append(randrange(0, 10))
    arr.append(vararr)
print(arr)
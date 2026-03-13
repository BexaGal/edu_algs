from random import randrange
lines = int(input("Enter matrix lines: "))
rows = int(input("Enter matrix rows: "))
arr = []
for i in range(lines):
    vararr = []
    for j in range(rows):
        vararr.append(randrange(1, 100))
    arr.append(vararr)

for i in range(lines):
    if i % 2 != 0 and arr[i][0] > arr[i][rows - 1]:
        print(arr[i])

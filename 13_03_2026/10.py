from random import randrange
lines = int(input("Enter matrix lines: "))
rows = int(input("Enter matrix rows: "))
arr = []
for i in range(lines):
    vararr = []
    for j in range(rows):
        vararr.append(randrange(1, 100))
    arr.append(vararr)

counter = 0
for i in range(lines):
    for j in range(rows):
        if arr[i][j] == 7:
            counter += 1

print(counter)
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
    print(arr[i])

for i in range(lines):
    varstring = ""
    if i % 2 == 0:
        for j in range(rows):
            varstring += str(arr[i][j]) + " "
    else:
        for j in range(rows - 1, -1, -1):
            varstring += str(arr[i][j]) + " "
    print(varstring)
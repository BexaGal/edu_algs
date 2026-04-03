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

k = int(input("line to show: "))
p = int(input("row to show: "))

print(arr[k])
rowstr = ""
for i in range(lines):
    rowstr += str(arr[i][p]) + " "
print(rowstr)
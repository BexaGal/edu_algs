size = int(input("Enter matrix size: "))
arr = []
for i in range(size):
    vararr = []
    for j in range(size):
        if i == 0 or i == (size - 1) or j == 0 or j == (size - 1):
            vararr.append(1)
        else:
            vararr.append(0)
    arr.append(vararr)


for i in range(size):
    print(arr[i])
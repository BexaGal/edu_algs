size = int(input("Enter matrix size: "))
arr = []
for i in range(size):
    vararr = []
    for j in range(size):
        if i == j:
            vararr.append(3)
        elif j > i:
            vararr.append(2)
        else:
            vararr.append(1)
    arr.append(vararr)

for i in range(size):
    print(arr[i])
arr = [
    [-8, -14, -19, -18],
    [25, 28, 26, 20],
    [11, 18, 20, 25]
]
print(arr[1][3], arr[2][0])
second = ""
for i in range(3):
    second += str(arr[i][1]) + " "
print(second)
avg3 = 0
for i in range(4):
    avg3 += arr[2][i]
print(avg3/3)
for i in range(3):
    for j in range(4):
        if arr[i][j] <= 26 and arr[i][j] >= 24:
            print("In station " + str(i) + " with temperature " + str(arr[i][j]))
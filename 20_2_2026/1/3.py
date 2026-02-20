a = []
for i in range(10):
    a.append(int(input()))
    if a[i] <= 0 or a[i] > 1000:
        print("Illegal number")
        exit()
curmin = 1001
for i in range(len(a)):
    if a[i] < curmin and a[i] % 2 == 0 and not(a[i] % 3 == 0):
        curmin = a[i]
if curmin == 1001:
    print("No numbers found")
    exit()
print(curmin)

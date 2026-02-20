n = int(input("Enter number: "))
print(len(str(n)))
tmp = abs(n)
if tmp == 0:
    print(0)
    exit()
num = 0
while tmp > 0:
    tmp = tmp // 10
    num += 1
print(num)

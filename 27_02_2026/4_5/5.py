a = []
first = int(input("Enter the first element: "))
difference = int(input("Enter the difference: "))
r = int(input("Input the number of elements: "))
a = [first]
cur = 0
for i in range(r-1):
    a.append(a[i] + difference)
print(a)

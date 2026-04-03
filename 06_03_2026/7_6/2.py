from random import randrange
nmbr = int(input("Enter number in range 1..4: "))
a = []
result = ""
for i in range(10):
    a.append(randrange(1, 5))
    if a[i] == nmbr:
        result = result + str(i) + " "
print(a)
print(result)

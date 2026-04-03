from random import randrange
a = []
for i in range(10):
    a.append(randrange(1, 100))
for i in range(len(a)):
    swapped = False
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swapped = True
    if not swapped: break
print(a)

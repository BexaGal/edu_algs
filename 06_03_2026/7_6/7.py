from random import randrange
a = []
for i in range(10):
    a.append(randrange(1, 100))
unique = 0
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

for i in range(len(a) - 1):
    if a[i] != a[i+1]:
        unique += 1

print(a)
print(unique)

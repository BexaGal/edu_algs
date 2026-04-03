from random import randrange
a = []
for i in range(10):
    a.append(randrange(1, 100))
b = []
for i in range(len(a)):
    b.append(i)

for i in range(len(b)):
    for j in range(len(b) - 1):
        if a[b[j]] > a[b[j+1]]:
            b[j], b[j+1] = b[j+1], b[j]
print(a)
print(b)

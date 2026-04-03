from random import randrange
a = []
for i in range(10):
    a.append(randrange(1, 100))
print(a)
maxindex = 0
for i in range(10):
    if a[i] >= a[maxindex]:
        maxindex = i
print(maxindex)
var = 0
for i in range(maxindex, 0, -1):
    var = a[i-1]
    a[i-1] = a[i]
    a[i] = var
print(a)

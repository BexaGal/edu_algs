from random import randrange
a = []
for i in range(100):
    a.append(randrange(1, 100))
firstmin = 0
lastmost = 0
for i in range(len(a)):
    if a[i] < a[firstmin]:
        firstmin = i
    if a[i] >= a[lastmost]:
        lastmost = i
print(a)
print("First minimum's index: " + str(firstmin))
print("Last maximum's index: " + str(lastmost))

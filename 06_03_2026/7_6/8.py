from random import randrange
a = []
for i in range(20):
    a.append(randrange(1, 10))
a = sorted(a)
ser = []
serlen = []
for i in range(0, len(a) - 1):
    curlen = 0
    if i != 0:
        if a[i] == a[i+1] and a[i] != a[i-1]:
            for j in range(i, len(a)):
                if a[i] == a[j]:
                    curlen += 1
                else: break
            ser.append(a[i])
            serlen.append(curlen)
    else:
        if a[i] == a[i+1]:
            for j in range(i, len(a)):
                if a[i] == a[j]:
                    curlen += 1
                else: break
            ser.append(a[i])
            serlen.append(curlen)

print(a)
print(ser)
print(serlen)

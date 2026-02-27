a = []
for i in range(1000, 10000):
    if len(list(set(str(i)))) == 4:
        a.append(i)
print(a)

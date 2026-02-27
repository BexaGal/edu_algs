a = []
for i in range(1000, 10000):
    if not ("2" in str(i) or "7" in str(i)):
        a.append(i)
print(a)

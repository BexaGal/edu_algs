a = []
for i in range(10):
    vara = []
    for j in range(10):
        if i == j:
            vara.append(0)
        else:
            vara.append(1)
    a.append(vara)
for i in range(10):
    print(a[i])

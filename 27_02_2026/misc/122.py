a = []
for i in range(1, 11):
    vara = []
    for j in range (1, 11):
        vara.append(str(i) + "x" + str(j) + "="+  str(i*j))
    a.append(vara)
for i in range(len(a)):
    print(a[i])

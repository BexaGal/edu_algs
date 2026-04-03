from random import randrange
matr = []
for i in range(10):
    vararr = []
    for j in range(10):
        vararr.append(randrange(1, 100))
    matr.append(vararr)

for i in range(10):
    print(matr[i])

minimum = {"0": matr[0][0], "1": [0, 0]}
maximum = {"0": matr[0][0], "1": [0, 0]}

for i in range(10):
    for j in range(10):
        if minimum["0"] > matr[i][j]:
            minimum = {"0": matr[i][j], "1": [i, j]}
        if maximum["0"] < matr[i][j]:
            maximum = {"0": matr[i][j], "1": [i, j]}

print("Min: " + str(minimum["0"]) + " at index " + str(minimum["1"]))
print("Max: " + str(maximum["0"]) + " at index " + str(maximum["1"]))
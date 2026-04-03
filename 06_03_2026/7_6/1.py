from random import randrange
a = []
for i in range(10):
    a.append(randrange(1, 4))
    if a[i] % 3 == 0:
        print(a)
        print("CATCH!")
        exit()
print("No")

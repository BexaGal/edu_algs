from random import randrange
r = int(input("Number of elements: "))
a = []
even = 0
odd = 0
for i in range(r):
    a.append(randrange(20, 101))
    if a[i] % 2:
        even += 1
    else:
        odd += 1
print(a)
print("Evens", even)
print("Odds", odd)

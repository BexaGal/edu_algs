from random import randrange
arr = []
for i in range(10):
    arr.append(randrange(0, 100))

arr.sort()
print("Least precipitation: " + str(arr[0]))
print("Most precipitation: " + str(arr[9]))
print(arr)

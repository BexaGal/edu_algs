from random import randrange
def partition(arr, low, high):
    pivot = a[randrange(low, high)]
    i = low
    j = high
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)


a = []
for i in range(10):
    a.append(randrange(1, 100))

for i in range(len(a)):
    swapped = False
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swapped = True
    if not swapped: break

print(a)

severalmax = 0
for i in range(len(a) - 1):
    if a[i] == a[i+1] and a[i] > severalmax:
        severalmax = a[i]
print(severalmax)

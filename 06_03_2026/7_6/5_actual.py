from random import randrange
def partition(arr, low, high):
    pivot = int(str(a[randrange(low, high)])[0])
    i = low
    j = high
    while True:
        while int(str(arr[i])[0]) < pivot:
            print(i)
            i += 1
        while int(str(arr[j])[0]) > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)


a =[]
for i in range(10):
    a.append(randrange(1, 100))
quicksort(a, 0, len(a) - 1)
print(a)

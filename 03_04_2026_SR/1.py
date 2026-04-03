from random import randrange
arr = []
# имя заменено на номер студента
# Массив двумерный именно потому что вместо номера должно было быть имя
# Можно было бы использовать словарь или кортежи
for i in range(20):
    arr.append([i, randrange(2, 6)])

for i in range(len(arr)):
    if arr[i][1] == 2:
        print(arr[i][0])

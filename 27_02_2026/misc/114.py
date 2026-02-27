def divisible_by_all_list(number, list_of_divisers, target=0):
    for i in list_of_divisers:
        if number % i != target:
            return False
    return True


i = 11
a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    if i % 11 == 0 and divisible_by_all_list(i, a, 1):
        print(i)
        break;
    i += 1


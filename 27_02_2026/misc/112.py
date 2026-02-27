for i in range (100, 1000):
    if i == sum(pow(int(digit), 3) for digit in str(i)):
        print(i)

for i in range(10000, 100000):
    if i%4 == 0 and int(str(i)[0])%2 != 0 and (sum(int(digit) for digit in str(i)))%2 == 0:
        print(i)

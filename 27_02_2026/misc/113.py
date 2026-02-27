counter = 0
for i in range(1000, 10000):
    if i / sum(int(digit) for digit in str(i)) == 600:
        print(i)
        counter += 1
print(counter)

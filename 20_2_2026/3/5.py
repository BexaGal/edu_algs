num = int(input())
if num < 100 or num > 999:
    print("Invalid number")
    exit()
a, b, c = str(num)[0], str(num)[1], str(num)[2]
print(a + b + c)
print(a + c + b)
print(b + a + c)
print(b + c + a)
print(c + a + b)
print(c + b + a)

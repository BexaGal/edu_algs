def power(number, pwr):
    answer = 1
    for i in range(pwr):
        answer = answer * number
    return answer
n = int(input("Number: "))
p = int(input("Power: "))
print(power(n, p))

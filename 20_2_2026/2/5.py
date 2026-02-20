def fact(n):
    ans = 1
    for i in range(n):
        ans = ans * (i + 1)
    return(ans)

number = int(input())
print(fact(number))

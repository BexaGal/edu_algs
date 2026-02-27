ans = 0
for i in range(10, 0, -1):
    varstring = ""
    for j in range(i):
        varstring += str(i)
    print(varstring)
    ans += int(varstring)
print(ans)

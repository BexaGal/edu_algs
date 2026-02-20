def reverse(n):
    var = ""
    for i in range(len(str(n))):
        var = str(n)[i] + var
    return int(var)
num = int(input())
reversen = str(reverse(num))
print(reversen)
for i in range(len(reversen)):
    print(str(reversen)[i])

def is_automorph(num):
    numsq = num*num
    return str(numsq).endswith(str(num))

trsh = int(input())

for i in range(trsh):
    if is_automorph(i):
        print(i)

var1 = 0
var2 = 1
trsh = int(input("Threshold: "))
if trsh in [0, 1] or trsh < 0:
    print("Illegal number:")
    exit()
print(str(var1) + "\n" + str(var2))
for i in range(trsh - 2):
    intr = var2
    var2 = var1 + var2
    var1 = intr
    print(var2)

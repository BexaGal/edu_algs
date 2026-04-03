from random import randrange
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(7):
    varstr = ""
    for j in range(7):
        varstr += alphabet[randrange(len(alphabet))]
    print(varstr)
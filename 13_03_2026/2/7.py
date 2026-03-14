alphabet = "abcdefghijklmnopqrstuvwxyz"
i = 0
while i < len(alphabet):
    varstr = ""
    for j in range(5):
        if i < len(alphabet):
            varstr += alphabet[i]
            i += 1
        else: break

    print(varstr)
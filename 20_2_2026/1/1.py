possum = 0
negsum = 0
var = 1
while var != 0:
    var = int(input("Enter number: "))
    if var > 0:
        possum += var
    elif var < 0:
        negsum += var
    else:
        break
print("Positives: ", possum)
print("Negatives: ", negsum)

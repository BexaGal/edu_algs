summ = 0
numm = 0
curn = 0
while True:
    curn = str(input("Enter number. To exit type \"done\": " ))
    if curn.lower() == "done":
        break
    numm += 1
    summ += int(curn)
try:
    print(summ/numm)
except:
    print("No numbers were added")

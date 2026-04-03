from random import randrange
alphabet = "abcdefghijklmnopqrstuvwxyz"
ran = randrange(3, 11)
string = ""
full = 0
for i in range(ran):
    chance = ran - i
    if randrange(0, chance) == 0 and full < 2:
        string += "!"
        full += 1
    else:
        string += alphabet[randrange(len(alphabet))]
print(string)
alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

createf = open("2.infile", "a")
createf.close()

f = open("2.infile", "rt")

symbols = 0
nums = 0
lines = 0

for line in f:
    lines += 1
    for i in range(len(line)):
        if line[i].lower() in alphabet:
            symbols += 1
        if line[i] in numbers:
            nums += 1

print("Lines: " + str(lines))
print("Symbols: " + str(symbols))
print("Numbers: " + str(nums))

f.close()
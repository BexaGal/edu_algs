alphabet = "abcdefghijklmnopqrstuvwxyzabc"
letter = str(input())

for i in range(len(alphabet)):
    if letter.lower() == alphabet[i]:
        print(alphabet[i], alphabet[i+1], alphabet[i+2], alphabet[i+3])
        break
s = "1+25+3"
s = s.split("+")
s = [int(i) for i in s]
print(sum(s))

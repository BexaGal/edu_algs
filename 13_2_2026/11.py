import math
kat1 = float(input())
kat2 = float(input())
area = kat1*kat2/2
hyp = math.sqrt( kat1*kat1 + kat2*kat2)
print("area: " + str(area))
print("Hyp: " + str(hyp) )
print("Prmt: " + str(hyp + kat1 + kat2))

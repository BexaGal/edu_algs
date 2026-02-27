distance = 5
increment = 1.05
days = int(input("Days of training: "))
maxrange = 100
distlog = [distance]
for i in range(1, days):
    distlog.append(distlog[i-1] * increment)
print("Distance log:", distlog)
if days < 5:
    print("Not enough days for 5 day log")
else:
    sumforfive = 0
    for i in range(5):
        sumforfive += distlog[i]
    print("Distance for 5 days:", sumforfive)
sumfordays = 0
for i in range(days):
    sumfordays += distlog[i]
print("Distance for", days, "days:", sumfordays)
counter = 0
vardis = 5
while vardis < 100:
    vardis = vardis*increment
    counter += 1
print("Max days until 100km distance hit:", counter)

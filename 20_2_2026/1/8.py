weekdays = ["Mon", "Tue", "Wen", "Thu", "Fri", "Sat", "Sun"]
for i in range(len(weekdays)):
    if i < 5:
        print(str(i+1) + " " + weekdays[i] + "  Workday")
    else:
        print(str(i+1) + " " + weekdays[i] + "  Weekend")

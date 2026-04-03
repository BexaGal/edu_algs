class applicants:
    def __init__(self, name, surname, year, weight, height):
        self.name = name
        self.surname = surname
        self.year = year
        self.weight = weight
        self.height = height

curyear = 2026

apps = [
    applicants("Илья", "Тувалов", 2016, 48, 157),
    applicants("Артём", "Сафин", 2018, 39, 146),
    applicants("Ильдан", "Гиниатуллин", 2014, 54, 163),
    applicants("Диас", "Яруллин", 2016, 43, 156),
    applicants("Роман", "Aлиев", 2017, 44, 158)
]

apps.sort(key=lambda x: x.surname)

for i in range(len(apps)):
    if (curyear-apps[i].year) >= 9 and (curyear-apps[i].year) <= 11 and apps[i].weight <= 45 and apps[i].height >= 155:
        print(apps[i].name, apps[i].surname)

class toy:
    def __init__(self, name, price, lowerage, maxage):
        self.name = name
        self.price = price
        self.lowerage = lowerage
        self.maxage = maxage

toys = [
    toy("Конструктор", 11000, 8, 16),
    toy("Кукла", 1200, 3, 10),
    toy("Машинка", 800, 5, 12),
    toy("Солдатики", 900, 8, 12),
    toy("Кубики", 200, 1, 6),
    toy("Азбука", 300, 1, 10),
    toy("Барабаны", 14000, 4, 16)
]

maxprice = int(input())

toys.sort(key=lambda x: x.name)

for i in range(len(toys)):
    if toys[i].price <= maxprice and toys[i].lowerage <= 5 and toys[i].maxage >= 5:
        print(toys[i].name)

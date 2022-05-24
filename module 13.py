ticket = int(input("Введите количество билетов"))
s = 0
for i in range(ticket):
    age = int(input("Введите возраст"))
    if age < 18:
        s += 0
    elif 18 <= age < 25:
        s += 990
    else:
        s += 1390
if ticket > 3:
    d = 0.9
else:
    d = 1
print("Сумма к оплате:", s * d)
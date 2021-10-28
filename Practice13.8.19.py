tickets = int(input("Количество билетов: "))
price = 0
for i in range(tickets):
    age = int(input("Возраст поcетителя: "))
    if 18 <= age <= 25:
        price += 990
    elif age > 25:
        price += 1390
print("Cумма к оплате", price)
skidka = price * 0.1
if tickets >= 3:
    price = price - skidka
print('Сумма скидки', skidka)
print('Сумма со скидкой', price)
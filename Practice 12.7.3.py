per_cent = {'ТКБ':5.6 , 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = 100000#float(input("Ввести сумму вклада: "))
deposit=[] # накопленные средства за год вклада в каждом из банков

for i in per_cent.values():
    deposit.append(money * i / 100)

deposit_max = max(deposit)

print(deposit)
print("Максимальная сумма, которую вы можете заработать:", deposit_max)

print("Банк с максимальной суммой, которую вы можете заработать:", list(per_cent.keys())[deposit.index(deposit_max)])


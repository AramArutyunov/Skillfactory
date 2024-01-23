money = float(input("Введите число "))
per_cent = {"ТКБ": 5.6, "СКБ": 5.9, "ВТБ": 4.28, "СБЕР": 4.0}

# Значения из справочника переведены в список
percent_list = per_cent.values() 

# Определяем доход по каждому значению
deposit = [x * money / 100 for x in percent_list]

# Округляем значения в списке до целого чесла
deposit = list(map(round, deposit))

# определяем максимальное значение
deposit_i = max(deposit)

print(deposit)

print("Максимальная сумма, которую вы можете заработать", deposit_i)

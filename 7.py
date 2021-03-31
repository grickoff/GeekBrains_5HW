import json
# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

f = open('HW7.txt', 'r', encoding='utf-8')
hw = open('hw.txt', 'w', encoding='utf-8')
custom_dict = {}
custom_list = []
profits = []
counter = 0

for line in f:
    line = line.split()
    profit = int(line[2]) - int(line[3])
    custom_dict.update({line[0] : profit})

custom_list.append(custom_dict)

for i in custom_list:
    for numbers in map(int, i.values()):
        if numbers >= 0:
            profits.append(numbers)
            counter += 1

total_profit = {'avarege_profit': round(sum(profits) / counter)}
custom_list.append(total_profit)
print(custom_list)
json.dump(custom_list, hw)

f.close()
hw.close()




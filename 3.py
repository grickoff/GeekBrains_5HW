from random import randrange

# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

some_funny_thing = [' бомжует', ' не доедает', ' спит на вокзале', ' экономит на гречке', ' ест дворовых собак']
file = open('HW3.txt', 'r', encoding='utf-8')
text = file.read().split('\n')
work_dict = {}

for i in text:
    name = i.split()[0]
    money = float(i.split()[1])
    work_dict.update({name : money})
    if money <= 20.0:
        print(name, some_funny_thing[randrange(3)])

print('Реестр заработной платы: \n', work_dict)
print(f'Средний по заводу: {round(sum(work_dict.values())/len(work_dict.values()))}')

file.close()
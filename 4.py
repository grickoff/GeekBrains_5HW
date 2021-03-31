# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file = open('HW4.txt', 'r', encoding='utf-8')
my_list = []
b = 0

dict_list = file.read().split()
for i in dict_list:
    try:
        i = dictionary[i]
        my_list.append(dictionary[i])
        b += 1
        if b == 3:
            my_list.append('\n')
            b = 0
    except KeyError:
        i = i
        my_list.append(i)
print(my_list)

file.close()

file_2 = open('HW4.txt', 'w', encoding='utf-8')
file_2.writelines(my_list)
file_2.close()

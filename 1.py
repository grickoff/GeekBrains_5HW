# Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем.Об окончании ввода данных свидетельствует пустая строка.

f = open('HW1.txt', 'w')
write = []
while write != (''):
    write = input('Вводите построчно данные или оставьте поле ввода пустым для завершения: ')
    f.writelines( f'\n {write}')

f.close()
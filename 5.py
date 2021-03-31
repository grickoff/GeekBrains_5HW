# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

f = open('HW5.txt', 'w+')
f.write('3 4 7')
f.close()

f = open('HW5.txt', 'r')
custom_list = f.read().split()
print(custom_list)
sum_number = sum(int(i) for i in custom_list)
print(sum_number)

f.close()
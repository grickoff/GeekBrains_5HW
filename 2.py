# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file = open('HW2.txt', 'r')
strings = 0

while True:
    text = file.readline().split()
    if len(text) == 0:
        break
    print(text)
    print(f'слов - {len(text)} ')
    strings += 1

file.close()
print(strings, ' строк всего')
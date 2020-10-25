'''
Вариант 11:
Вам дана последовательность строк. Выведите строки, содержащие текст в круглых скобках.
'''

contents = []
while True:
    text = input('Введите строку или ОТМЕНА для отмены: ')
    if text == 'ОТМЕНА':
        break
    else:
        contents.append(text) 
        
for line in contents:
    if 'Рисунок' in line:
        new_line = line.replace('Рисунок', 'Фото')
        print(new_line)
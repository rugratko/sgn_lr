'''
Вариант 11:
Вам дана последовательность строк. Выведите строки, содержащие текст в круглых скобках.
'''

contents = []
while True:
    text = input('Введите строку или ОТМЕНА для отмены')
    if text == 'ОТМЕНА':
        break
    else:
        contents.append(text)

for line in l:
    for i in "()":
        if i in line:
        	print(line)

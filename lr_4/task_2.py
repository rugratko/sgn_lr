'''
Индивидуальное задание №2. 
Выполнить согласно номеру варианта по журналу.

Вариант 11
1 Найти наибольший элемент списка, который делится на 2 без остатка и вывести его на экран.
'''

start = -209
end = 194
step = 13

custom_list = [i for i in range(start, end + 1, step)] #генератор списка согласно условия

even_num_list = []
for i in custom_list:
    if i % 2 == 0:
        even_num_list.append(i)
        
if len(even_num_list):
    print('Наибольшее четное число:', max(even_num_list))
else:
    print('Четных чисел нет')

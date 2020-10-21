'''
Индивидуальное задание №3. 
Выполнить согласно номеру варианта по журналу.

Вариант 11
2. Дан одномерный массив целого типа. Получить другой массив, состоящий только из четных чисел исходного массива, меньше 10, или сообщить, что таких чисел нет. 
   Полученный массив вывести в порядке возрастания элементов.
'''

start = -209
end = 194
step = 13

custom_list = [i for i in range(start, end + 1, step)] #генератор списка согласно условия

even_num_list = []
for i in custom_list:
    if i % 2 == 0 and i < 10:
        even_num_list.append(i)
        
if len(even_num_list):
    even_num_list.sort()
    print('Отсортированный массив:', even_num_list)
else:
    print('Четных чисел меньше 10 в исходном массиве нет')
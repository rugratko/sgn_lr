'''
11.	Создать множество на основе двух списков чисел: 
в множество войдут все элементы первого списка, которых нет во втором списке.
'''

set_1 = set(i for i in range(10))
set_2 = set(i for i in range(5))
print(set_1, set_2)
set_1.difference_update(set_2)
print(set_1)
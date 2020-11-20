import random

mas = []
a = 1
while a != 0:
    a = int(input('Введите число (0 чтобы прервать): '))
    mas.append(a)
print('Исходный массив: ', mas)
    
for i in range(len(mas)):
    if mas[i] < 0:
        mas[i] = random.randint(1, 10)

print('Конечный массив: ', mas)

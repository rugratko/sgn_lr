'''
Индивидуальное задание №1. 
Вывести на экран последовательность чисел в прямом и в 
обратном порядке согласно номера варианта по журналу, используя оператор for и функцию range().

Можно сделать через списки
'''

def counter(start, end, step):
    for i in range(start, end + 1, step): #компенсируем невхождение последнего числа в ряд
        print(i, end = ' ') # end - метод функции print, позволяет указать конец сообщения (обычно там стоит перенос)
    print('\n')
    step = step * (-1) #разворачиваем счетчик
    for i in range(end, start - 1, step): #опять компенсируем, только уже для первого числа
        print(i, end = ' ')

# start = int(input('Введите число начала отсчета: '))
# end = int(input('Введите число конца отсчета: '))
# step = int(input('Введите шаг отсчета: '))

start = -209
end = 194
step = 13

counter(start, end, step)
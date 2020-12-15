'''
Программа 1. Дан словарь. Написать программу записи словаря в файл.
Программа 2. Написать программу:
- чтение словаря из файла, вывод на экран в отформатированном виде;
- добавление элемента в словарь (поля заполняются с консоли), вывод на экран;
- записи словаря в файл.
В программе должны быть функции 1) чтение словаря из файла, 2) записи в файл, 3) добавление пары в словарь.

Вариант 11. Словарь содержит пары

ID : [ ФИО, возраст, индекс группы ]
"4" : ["Иванов И.И.", 19, "ИУ5-11Б" ],
"1" : ["Петров М.Ф.", 22, "СГН2-11Б"],
"88" : ["Семенов П.С.", 18, "МТ5-32Б" ],
"35" : ["Успенская В.С.",21, "СМ1-51" ],
"70" : ["Говорова У.Я.", 18, "ФН2-31М" ]
'''
import pickle


students = [
    {4: ["Иванов И.И.", 19, "ИУ5-11Б"]},
    {1: ["Петров М.Ф.", 22, "СГН2-11Б"]},
    {88: ["Семенов П.С.", 18, "МТ5-32Б"]},
    {35: ["Успенская В.С.",21, "СМ1-51"]},
    {70: ["Говорова У.Я.", 18, "ФН2-31М"]}
]


def dprint():
    print("ID студента".ljust(15, ' '), "ФИО студента".ljust(20, ' '), "Возраст".ljust(15, ' '), "Группа".ljust(15, ' '))
    for student in students:
        for key, value in student.items():
            print(str(key).ljust(15, ' '), value[0].ljust(20, ' '), str(value[1]).ljust(15, ' '), value[2].ljust(15, ' '))


def dwrite():
    f = open('File', 'wb')
    pickle.dump(students, f)
    
    
dprint()
dwrite()
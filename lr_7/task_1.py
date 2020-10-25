print( "1&3. Создание множеств с помощью конструктора, генератора" )
a_set, b_set = set( 'любое множество' ), set( 'любое множество' )
print(a_set, b_set)

print( "2. Изменяет множество a_set с помощью методов " )
test = {5, 6, 10, 15, 20}
a_set.update(test)
print(a_set)

print( "4. Выполняет над множествами a_set и b_set операции " )
print(a_set.intersection(b_set))

print('5. Создает словарь a_dict с помощью литерала')
d1 = {'model': '4451', 'ios': '15.4'}
d2 = {'android': '7.1', 'windows': '10'}
print(d1, d2)

print('6. Выполняет следующие методы словаря a_dict')
print(d1.items())
d1.popitem()
print(d1)
d1.update(d2)
print(d1)


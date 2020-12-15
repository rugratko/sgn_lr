'''
11. Даны два предложения.
В каком из них доля (в %) буквы «о» больше?
В программе определить и использовать функцию
для расчета доли некоторой буквы в предложении.
'''


def count_letters(sent, letter):
    counter = 0
    for element in sent:
        if element == letter:
            counter += 1
    return (round(counter/len(sent), 3) * 100)


def comparation(sent_1, sent_2, letter):
    perc_1 = count_letters(sent_1, letter)
    perc_2 = count_letters(sent_2, letter)
    if perc_1 > perc_2:
        print('В первом предложении {}% букв, во втором - {}%. В первом больше'.format(perc_1, perc_2))
    elif perc_1 < perc_2:
        print('В первом предложении {}% букв, во втором - {}%. Во втором больше'.format(perc_1, perc_2))
    elif perc_1 == perc_2:
        print('В первом предложении {}% букв, во втором - {}%. Числа равны'.format(perc_1, perc_2))

sent_1 = input('Введите первое предложение: ')
sent_2 = input('Введите второе предложение: ')
letter = input('Введите букву для подсчета: ')

comparation(sent_1, sent_2, letter)

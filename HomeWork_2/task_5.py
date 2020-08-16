"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

my_list = [7, 5, 3, 3, 2]
digit = int(input('Введите, пожалуйста, натуральное число: '))
if digit >= 0:
    if digit in my_list:
        ct = my_list.count(digit)
        ind = my_list.index(digit)
        my_list.insert(ind+ct, digit)
    elif digit > max(my_list):
        my_list.insert(0, digit)
    elif digit < min(my_list):
        my_list.append(digit)
    else:
        for ind, elem in enumerate(my_list):
            if digit > elem:
                my_list.insert(ind, digit)
                break
    print(my_list)

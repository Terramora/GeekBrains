"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(first, second):
    try:
        result = first // second
        print(f'Результат деления: {result}')
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')


division(first=int(input('Делимое:')), second=int(input('Делитель:')))

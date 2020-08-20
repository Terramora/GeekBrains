"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(var1, var2, var3):
    ls = [var1, var2, var3]
    ls.remove(min(ls))
    print(f"Сумма элементов '{ls}' = {sum(ls)}")


variables = input('Введите, пожалуйста, три числа через запятую, например, "1,2,3":')
variables = variables.split(',')
try:
    my_func(int(variables[0]), int(variables[1]), int(variables[2]))
except IndexError:
    print('Вы ввели недостаточное количество чисел!')

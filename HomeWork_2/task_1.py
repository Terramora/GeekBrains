"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
while True:
    var = int(input('Введите, пожалуйста, 0 или 1:'))
    if var in (0, 1):
        test_list = [var, str(var), bool(var), list(str(var + bool(var) + var)), float(var), {'var': var}, {var, bool(var)}, (var, str(var), bool(var)), None, bytes(var), bytearray(var)]
        print(test_list)
        for row in test_list:
            print(type(row))
        break

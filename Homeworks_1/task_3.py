"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

n = int(input('Введите, пожалуйста, число:'))
if n > 0:
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(f'Сумма: {(n1 + n2 + n3)}')
else:
    """
    Немного не соответствует условиям т.к должна происходить конкатенация,
    но сама по себе строка приобретает вид выражения '-3-3-3-3-3-3'.
    Сумма данного выражения будет: (-3) + (-3-3) + (-3-3-3).
    eval() опасен и не проходили, но очень хотелось попробовать решить и отрицательные числа.
    Не вышло :(
    Буду очень рад, если подскажите способы решения!
    """
    n1 = n
    n2 = int(eval(str(n) * 2))
    n3 = int(eval(str(n) * 3))
    print(f'Сумма: {(n1 + n2 + n3)}')

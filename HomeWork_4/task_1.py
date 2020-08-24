"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def input_data():
    try:
        st_name, hh, rate, revard = argv
        salary = int(hh) * int(rate) + int(revard)
        print(f'Зарплата до вычета: {salary} рублей')
        print(f'Зарплата после вычета: {int(salary * (1 - 13/100))} рублей')
    except ValueError as error:
        print(str(error))


input_data()

"""
Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
"""


class Cell:
    def __init__(self, cell, name):
        self.name = name
        if cell >= 0.01:
            self.cell = cell
        else:
            self.cell = 1
            print(f'{self.name}: Количество клеток не может быть меньше 0.01\nВыставлено значение по умолчанию\ncell = 1')

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        result = self.cell - other.cell
        if result < 0:
            print(f'{self.name}: Клетка не может уйти в отрицательное значение')
            return 0
        else:
            return result

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return int(self.cell / other.cell)

    def make_order(self, cl, ct):
        cell = '*' * cl.cell
        st = ''
        for i, row in enumerate(cell, 1):
            if i % ct == 0:
                st += row + '\n'
            else:
                st += row
        return print(st)


c1 = Cell(5, 'c1')
print(c1.cell)
c2 = Cell(10, 'c2')
print(c2.cell)
c3 = Cell(c1 + c2, 'c3')
print(c3.cell)
c4 = Cell(c1 - c2, 'c4')
print(c4.cell)
c5 = Cell(c1 * c2, 'c5')
print(c5.cell)
c6 = Cell(c1 / c2, 'c6')
print(c6.cell)
c6.make_order(c3, 5)

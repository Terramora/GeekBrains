"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, cp1, cp2):
        self.cp1 = cp1
        self.cp2 = cp2
        """self.complex = self.cp1 + self.cp2 * 1j
        print(self.complex)"""

    def __add__(self, other):
        res1 = self.cp1 + other.cp2
        res2 = self.cp2 + other.cp1
        return '(' + str(res1) + '+' + str(res2) + 'j)'

    def __mul__(self, other):
        print('('+str(self.cp1 * other.cp1 - self.cp2 * other.cp2)+'+'+str(self.cp1 * other.cp2 + self.cp2 * other.cp1)+'j)')


cl1 = Complex(1, 2)
cl2 = Complex(1, 2)
cl1 + cl2
cl1 * cl2

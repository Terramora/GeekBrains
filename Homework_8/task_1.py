"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, date):
        self.str_date = date

    @classmethod
    def parser(cls, date):
        try:
            ls_date = list(map(int, date.split('-')))
        except ValueError:
            print(f'Вводить необходимо только числа!\n {date} некорректный формат')
            return [1, 1, 1900]
        else:
            return ls_date

    @staticmethod
    def validation(date):
        day, month, year = date
        print(f'Валидирую дату: {"-".join((list(map(str, date))))}')
        if 1 <= month <= 12 and 1 <= day <= 32 and len(str(year)) == 4:
            if month == 2:
                if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
                    if day > 29:
                        print('В феврале не может быть более 29-и дней')
                else:
                    if day > 28:
                        print('В феврале не может быть более 28-и дней')
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                if day > 31:
                    print('В этом месяце не может быть больше 31-го дня')
            elif month not in [1, 3, 5, 7, 8, 10, 12]:
                if day > 30:
                    print('В этом месяце не может быть больше 30-го дня')
            print('Валидация окончена')
        else:
            print('Некорректное значение даты.')


cl1 = Date(input('Введите дату в формате dd-mm-yyyy: '))
cl1.validation(cl1.parser(cl1.str_date))

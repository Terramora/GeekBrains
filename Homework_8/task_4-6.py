class OEW:
    warehouse = {'printer': 0, 'xerox': 0, 'scanner': 0}

    @classmethod
    def input(cls, product, i):
        if product == 1:
            cls.warehouse['printer'] += i
        elif product == 2:
            cls.warehouse['xerox'] += i
        elif product == 3:
            cls.warehouse['scanner'] += i
        else:
            print('Такого продукта нет!')
        print(cls.warehouse)
        print('Метод завершен\n')

    @classmethod
    def output(cls, product, i):
        if product == 1:
            if cls.warehouse['printer'] - i < 0:
                print(f'Осталось на складе: {cls.warehouse["printer"]}\nНе хватает оборудования для перемещения!')
            else:
                cls.warehouse['printer'] -= i
                Printer.available += i
        elif product == 2:
            if cls.warehouse['xerox'] - i < 0:
                print(f'Осталось на складе: {cls.warehouse["xerox"]}\nНе хватает оборудования для перемещения!')
            else:
                cls.warehouse['xerox'] -= i
                Xerox.available += i
        elif product == 3:
            if cls.warehouse['scanner'] - i < 0:
                print(f'Осталось на складе: {cls.warehouse["scanner"]}\nНе хватает оборудования для перемещения!')
            else:
                cls.warehouse['scanner'] -= i
                Scanner.available += i
        else:
            print('Такого продукта нет!')
        print('Метод завершен\n')


class TexOffice:
    available = 0

    def __init__(self, office):
        self.office = office

    @classmethod
    def show_tex(cls, text):
        print(f'{text} {cls.available}')


class Printer(TexOffice):

    def __init__(self, color):
        super(TexOffice, self).__init__()
        self.color = color


class Scanner(TexOffice):

    def __init__(self, types):
        super(TexOffice, self).__init__()
        self.types = types


class Xerox(TexOffice):

    def __init__(self, model):
        super(TexOffice, self).__init__()
        self.model = model


def interface():
    while True:
        print(
            'Для управления складом выберите один из предложенных пунктов.\n1 - добавление техники\n2 - инвентаризация\n3 - перемещение техники\n4 - выйти из меню')
        try:
            menu = int(input('Введите номер пункта:'))
            if menu == 1:
                try:
                    OEW.input(int(input('1 - Принтер\n2 - Ксерокс\n3 - Сканер')), int(input('Какое количество?')))
                except ValueError:
                    print('Необходимо вводить числа!')
            elif menu == 2:
                print(f'На складе: {OEW.warehouse}')
                Printer.show_tex('Количество принтеров:')
                Xerox.show_tex('Количество ксероксов:')
                Scanner.show_tex('Количество сканеров:')
            elif menu == 3:
                try:
                    OEW.output(int(input('1 - Принтер\n2 - Ксерокс\n3 - Сканер')), int(input('Какое количество?')))
                except ValueError:
                    print('Необходимо вводить числа!')
            elif menu == 4:
                print('Программа завершена!')
                break
            else:
                print('Пункт не найден')
        except ValueError:
            print('Некорректный ввод!')


interface()

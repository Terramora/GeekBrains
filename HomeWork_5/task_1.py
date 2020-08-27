"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def create_file(name):
    with open(f'{name}.txt', 'w+', encoding='utf-8') as file_name:
        while True:
            text = input('Введите любые данные или пустую строку для завершения:    ')
            if text:
                print(text, file=file_name)
            else:
                print('Содержание файла:')
                file_name.seek(0)
                for row in file_name:
                    print(row)
                return 


create_file('test')

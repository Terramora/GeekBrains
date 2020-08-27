"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def create_file(ls):
    with open('task_5.txt', 'w+', encoding='utf-8') as f:
        for row in ls:
            print(row, file=f)
        f.seek(0)
        sm = sum([int(row) for row in f])
        print(f'Сумма: {sm}')


create_file(input('Введите набор чисел через пробел: ').split())

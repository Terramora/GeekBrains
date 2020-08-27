"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""


def translate():
    rus = {'1': 'Один - 1', '2': 'Два - 2', '3': 'Три - 3', '4': 'Четыре - 4'}
    new_file = []
    with open('text_4.txt', 'r', encoding='utf-8') as f:
        for row in f:
            new_file.append(rus[row.replace('\n', '').replace(' ', '').split('-')[1]])
    with open('new_file.txt', 'w', encoding='utf-8') as new:
        for row in new_file:
            print(row, file=new)


translate()

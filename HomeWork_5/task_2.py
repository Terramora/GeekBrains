"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def get_file():
    with open('task_2.txt', 'r', encoding='utf-8') as t2:
        text = ''
        for i, row in enumerate(t2, 1):
            text += f'Строка #{i}: количество элементов в ней - {len(row.split())}\n'
        print(text)


get_file()

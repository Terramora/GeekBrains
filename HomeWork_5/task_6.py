"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
"""

import re


def get_file_re():
    with open('text_6.txt', 'r', encoding='utf-8') as f:
        dt = {}
        for row in f:
            ls = row.split(':')
            dt.update({ls[0]: sum(map(int, re.sub(r'[^0-9.]+', r' ', ls[1]).split()))})

        print(dt)


get_file_re()


def get_file_replace():
    with open('text_6.txt', 'r', encoding='utf-8') as f:
        dt = {}
        for row in f:
            ls = row.split(':')
            dt.update(
                {ls[0]: sum(map(int, ls[1].replace('(л)', ' ').replace('(пр)', ' ').replace('(лаб)', ' ').replace('-',
                                                                                                                  ' ').split()))})

        print(dt)


get_file_replace()

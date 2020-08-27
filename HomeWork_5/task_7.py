#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json


def get_data_company():
    with open('text_7.txt', 'r', encoding='utf-8') as f:
        av = []
        js = []
        dt = '{'
        for i, row in enumerate(f, 1):
            rs = row.split()
            profit = int(rs[2]) - int(rs[3])
            if profit > 0:
                av.append(profit)
            if i > 1:
                dt += ','
            dt += '"' + rs[0] + '": "' + str(profit) + '"'
        dt += '}'
        av = {'average_profit': sum(av) / len(av)}
        js.append(json.loads(dt))
        js.append(av)
        create_json(js)


def create_json(js):
    with open('task_7.json', 'w', encoding='utf-8') as f1:
        new_json = []
        for i, row in enumerate(js):
            new_json.append(json.dumps(row, ensure_ascii=False))
        print(new_json)
        print(new_json, file=f1)


get_data_company()

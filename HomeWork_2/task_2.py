"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

answer = list(input('Введите любое слово:'))
i = 0
while len(answer) > 1 and i < len(answer) - 1:
    answer[i], answer[i + 1] = answer[i + 1], answer[i]
    print(answer[i], answer[i + 1])
    i += 2

print(answer)

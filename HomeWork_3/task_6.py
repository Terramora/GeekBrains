"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(text):
    return text.title()


def check_ascii(text):
    result = True
    for row in text:
        if 65 < ord(row.upper()) > 90:
            return False
        else:
            pass
    return result


def main(text):
    text = text.split(' ')
    result = []
    for row in text:
        if check_ascii(row):
            result.append(int_func(row))
        else:
            print(f'"{row}" выходит из диапозона символов латиницы в ASCII!')
    print(' '.join(result))


main(input('Введите строку из слов, разделенную пробелом:'))

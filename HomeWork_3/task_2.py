"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def get_user_info(first_name, last_name, birthday, city, email, phone):
    print(
        f'Имя: {first_name}, фамилия: {last_name}, год рождения: {birthday}, город: {city}, email: {email}, номер телефона: {phone}')


schemas = {
    'Имя': '',
    'фамилия': '',
    'год рождения': '',
    'город': '',
    'email': '',
    'номер телефона': ''
}

for key in schemas:
    schemas[key] = input(f'Введите {key}:')

get_user_info(first_name=schemas['Имя'],
              last_name=schemas['фамилия'],
              birthday=schemas['год рождения'],
              city=schemas['город'],
              email=schemas['email'],
              phone=schemas['номер телефона'])

"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time
from colorama import Back, Fore

"""
Вывод работает только в консоль!
"""


class TrafficLight:

    def __init__(self, color):
        self.color = color.lower()
        self.timing = {'красный': 7, 'желтый': 2, 'зеленый': 7}

    def running(self):
        while True:
            if self.color == 'красный':
                for i in range(self.timing[self.color], 0, -1):
                    print(Fore.RED + f'Красный: {i}', end='\r', flush=True)
                    time.sleep(1)
                self.color = 'желтый'
            elif self.color == 'желтый':
                for i in range(self.timing[self.color], 0, -1):
                    print(Back.YELLOW + f'Желтый: {i}', end='\r', flush=True)
                    time.sleep(1)
                self.color = 'зеленый'
            elif self.color == 'зеленый':
                for i in range(self.timing[self.color], 0, -1):
                    print(Back.YELLOW + f'Зеленый: {i}', end='\r', flush=True)
                    time.sleep(1)
                break


lt = TrafficLight('Красный')
lt.running()

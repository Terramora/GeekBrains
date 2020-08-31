"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return print(f'{self.name} поехала!')

    def stop(self):
        return print(f'{self.name} остановилась!')

    def turn(self, direction):
        return print(f'{self.name} повернула  на {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость {self.name}: {self.speed}')
            print(f'Внимание! Нарушен скоростной режим!')
        else:
            print(f'Текущая скорость {self.name}: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость {self.name}: {self.speed}')
            print(f'Внимание! Нарушен скоростной режим!')
        else:
            print(f'Текущая скорость {self.name}: {self.speed}')


class PoliceCar(Car):
    pass


car = Car(50, 'blue', 'audi', False)
car.go()
car.turn('left')
car.show_speed()
car.stop()

town_car = TownCar(65, 'blue', 'bmw', False)
town_car.go()
town_car.show_speed()
town_car.turn('right')
town_car.stop()

sport = SportCar(120, 'red', 'audi rs5', False)
sport.go()
sport.show_speed()
sport.turn('кольцо')
sport.stop()

police = PoliceCar(110, 'black', 'mercedes amg', True)
police.go()
police.turn('audi rs5')
police.show_speed()
police.stop()

work = WorkCar(40, 'black', 'gazel', False)
work.go()
work.turn('left')
work.show_speed()
work.stop()
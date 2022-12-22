"""Написать класс Car
Конструктор класса принимает атрибуты:
color: str (цвет)
count_passenger_seats: int (количество пассажирских мест)
is_baby_seat: bool (наличие десткого кресла)
is_busy: bool (определяется внутри конструктора со значением False, не принимается на
вход)
"""
class Car:

    def __init__(self, color: str, count_passengers_seats: int, is_baby_seat: bool) -> None:
        self.color = color
        self.count_passengers_seats = count_passengers_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    """Написать магический метод __str__ выводящий форматированную строку с информацией
    об автомобиле"""

    def __str__(self) -> str:
        return f'{self.color=} {self.count_passengers_seats=} {self.is_baby_seat=} {self.is_busy=}'


"""Написать класс Taxi
Конструктор класса принимает атрибуты:
cars: list[Car] (список экземпляров класса Car)"""

class Taxi(object):

    def __init__(self, cars: list[Car]):
        self.cars = cars

    """Реализовать метод find_car
    На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
    наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
    На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
    свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
    подходящего автомобиля нет, метод должен возвращать None"""

    def find_car(self, count_passengers_seats: int, is_baby_seat: bool):
        for car in self.cars:
            if count_passengers_seats <= car.count_passengers_seats \
                    and car.is_baby_seat == is_baby_seat \
                    and not car.is_busy:
                car.is_busy = True
                return car
        return None


car1 = Car(color='white', count_passengers_seats=4, is_baby_seat=False)
car2 = Car(color='green', count_passengers_seats=2, is_baby_seat=True)
car2.is_busy = True
car3 = Car(color='black', count_passengers_seats=1, is_baby_seat=True)
taxi = Taxi([car1, car2, car3])
print(taxi.find_car(1, is_baby_seat=True))

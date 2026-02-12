"""
Доработайте класс `Vehicle`
"""

from abc import ABC

from homework_05.exceptions import LowFuelError, NotEnoughFuel, CargoOverload, NotStartedError

"""добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
weight - в тоннах
fuel - количество топлива (буду мерять в литрах, l)
fuel_consumption l/km
"""

class Vehicle(ABC):
    def __init__(self, ):
        self.weight = None
        self.started = False
        self.fuel = 100
        self.fuel_consumption = 10 #на 100 км
        self.location = None
        self.odometer = 0.0
        self.type = self.__class__.__name__.lower()


    """добавьте метод start. 
        При вызове этого метода необходимо проверить состояние started. 
            И если не started, то нужно проверить, что топлива больше нуля, и обновить состояние started, 
        иначе нужно выкинуть исключение exceptions.LowFuelError
        """
    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                return True
            else:
                raise LowFuelError()
        else:
            print('Vehicle already started')
            return True


    """добавьте метод `move`, который проверяет, 
      что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода), 
      и изменяет количество оставшегося топлива, иначе выкидывает исключение `exceptions.NotEnoughFuel`"""
    def move(self, distance):
        #distance: 1 = 1km, 10 = 10km
        if not self.started:
            raise NotStartedError()
        else:
            fuel_needed = distance * self.fuel_consumption / 100
            if fuel_needed > self.fuel:
                raise NotEnoughFuel()
            else:
                self.location = 'new_location'
                self.odometer += distance
                self.fuel = self.fuel - fuel_needed
                if self.fuel == 0:
                    self.started = False
                    print(f'out of fuel. engine stopped')
                return self.location, self.odometer

    def __repr__(self):
        return f'type: "{self.type}", fuel: {self.fuel}, location: {self.location}, odometer: {self.odometer} km'

veh1 = Vehicle()
veh1.start()
veh1.move(50)
print(veh1)
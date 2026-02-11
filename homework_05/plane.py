"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload

"""В модуле plane создайте класс Plane
класс Plane должен быть наследником Vehicle
добавьте атрибуты cargo и max_cargo классу Plane
добавьте max_cargo в инициализатор (переопределите родительский)
объявите метод load_cargo, который принимает число, проверяет, 
что в сумме с текущим cargo не будет перегруза, и обновляет значение, 
в ином случае выкидывает исключение exceptions.CargoOverload
"""

class Plane(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        self.cargo = 10
        self._initial_cargo = self.cargo # добавил чтобы вернуть значение карго, что было до обнуленя
        self.max_cargo = 1000.0
        self.fuel = 0
        self.fuel_consumption = 0
        self.location = None
        self.odometer = 0

    def load_cargo(self, add_cargo: float) -> float:
        total_cargo = self.cargo + add_cargo
        if total_cargo > self.max_cargo:
            raise CargoOverload(total_cargo)
        else:
            self.cargo = total_cargo
            return self.cargo

    def remove_all_cargo(self) -> float:
        self.cargo = self._initial_cargo
        return self.cargo


    """
объявите метод remove_all_cargo, который обнуляет значение cargo и возвращает значение cargo, 
которое было до обнуления
>> тут не очень понял зачем обнулять чтобы потом вернуть исходное значение, пока что сделал как понял
"""

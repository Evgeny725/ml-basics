"""
Создайте класс `Car`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.engine import Engine


"""В модуле car создайте класс Car
класс Car должен быть наследником Vehicle
добавьте атрибут engine классу Car
объявите метод set_engine, который принимает 
в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car"""

class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        self.engine = None

    def set_engine(self, engine: Engine) -> None:
        self.engine = engine


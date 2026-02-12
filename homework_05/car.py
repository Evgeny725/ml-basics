"""
Создайте класс `Car`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.engine import Engine


"""В модуле car создайте класс Car, класс Car должен быть наследником Vehicle
добавьте атрибут engine классу Car, объявите метод set_engine, который принимает 
в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car"""

class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        self.engine = None

    def set_engine(self, engine: Engine) -> None:
        self.engine = engine

    def __repr__(self):
        return f'vehicle "{self.type}", {self.engine}'


car1 = Car()

engine4 = Engine(2.0, 4)
engine6 = Engine(2.5, 6)

car1.set_engine(engine4)

car2 = Car()
car2.set_engine(engine4)

car3 = Car()
car3.set_engine(engine6)

if __name__ == '__main__':
    for car in [car1, car2, car3]:
        print(car)



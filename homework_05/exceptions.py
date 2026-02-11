"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class VehicleError(Exception):
    pass


class NotEnoughFuel(VehicleError):
    print('Not enough fuel to reach the destination')
    pass


class CargoOverload(VehicleError):
    print('Maximum weight for this vehicle is ..')
    pass


class LowFuelError(VehicleError):
    print('Low fuel. Please refuel the vehicle')
    pass

class NotStartedError(VehicleError):
    print('Need to start engine before moving on')
    pass

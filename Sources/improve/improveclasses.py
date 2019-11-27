from abc import ABCMeta, abstractmethod


class Vehicle(object):
    """A Vehicle for sale by Jeffco Car Dealership.

    Attributes:
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """
    __metaclass__ = ABCMeta  # Will make it an abstract class ... plus set one method as virtual
    _wheels = None
    _base_sale_price = None

    def __init__(self, miles=None, make=None, model=None, year=None, sold_on=None):
        """Return a new Vehicle object."""
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    @abstractmethod
    def vehicle_type(self):
        """Return a string representing the type of vehicle ( implemented by child classes ) """
        pass

    @staticmethod
    def make_sound():
        print('room room')

    @classmethod
    def is_motorcycle(cls):
        return cls._wheels == 2

    @classmethod
    def is_car(cls):
        return cls._wheels == 4

    @classmethod
    def is_truck(cls):
        return cls._wheels > 4

    def sale_price(self):
        """Return the sale price for this car as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self._wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the car."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self._base_sale_price - (.10 * self.miles)


class Car(Vehicle):
    """A car for sale by Jeffco Car Dealership.
    """
    _wheels = 4
    _base_sale_price = 8000

    def vehicle_type(self):
        return 'I am a Car'


class Truck(Vehicle):
    """A car for sale by Jeffco Car Dealership.
    """
    _wheels = 8
    _base_sale_price = 10000

    def vehicle_type(self):
        return 'I am a Truck'


class Motorcycle(Vehicle):
    """A car for sale by Jeffco Car Dealership.
    """
    _wheels = 2
    _base_sale_price = 5000

    def vehicle_type(self):
        return 'I am a Truck'

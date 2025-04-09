# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Derived class for Cars
class Car(Vehicle):
    def __init__(self, make, model, year, vehicle_type):
        super().__init__(make, model, year)
        self.vehicle_type = vehicle_type

    def car_specific_info(self):
        return f"This car is a {self.vehicle_type}."
    
# Derived class for motorbikes
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike  # e.g., "Road Bike" or "Mountain Bike"

    def bike_specific_info(self):
        return f"This bike is a {self.type_of_bike}."
    
car = Car("Toyota", "Prado", 2022, "SUV")
print(car.display_info())
print(car.car_specific_info())



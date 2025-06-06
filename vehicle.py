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

# Polymorphic function
def print_vehicle_info(vehicle):
    print(vehicle.display_info())

# Derived class for Motorbikes
class Motorbike(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type  # e.g., "Sport Bike", "Cruiser", "Off-road"

    def bike_specific_info(self):
        return f"This motorbike is a {self.bike_type}."

# Polymorphic function
def print_vehicle_info(vehicle):
    print(vehicle.display_info())

# Example usage
car = Car("Toyota", "Prado", 2022, "Diesel")
print_vehicle_info(car)  # Calls display_info() method from Car
print(car.car_specific_info())

motorbike = Motorbike("Yamaha", "MT-07", 2021, "Sport Bike")
print_vehicle_info(motorbike)  # Calls display_info() method from Motorbike
print(motorbike.bike_specific_info())  # Calls bike_specific_info() specific to Motorbike

# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

    def start_engine(self):
        return f"Starting the engine of {self.make} {self.model}..."

# Derived class for Cars
class Car(Vehicle):
    def __init__(self, make, model, year, vehicle_type):
        super().__init__(make, model, year)
        self.vehicle_type = vehicle_type

    def car_specific_info(self):
        return f"This car is a {self.vehicle_type}."

    # Overriding the start_engine method
    def start_engine(self):
        return f"Starting the car engine for {self.make} {self.model}. Ready to drive!"

# Derived class for Motorbikes
class Motorbike(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def bike_specific_info(self):
        return f"This motorbike is a {self.bike_type}."

    # Overriding the start_engine method
    def start_engine(self):
        return f"Revving up the motorbike engine for {self.make} {self.model}. Ready to ride!"

# Polymorphic function
def print_vehicle_info(vehicle):
    print(vehicle.display_info())

# Example usage
car = Car("Toyota", "Prado", 2022, "Diesel")
print(print_vehicle_info(car))  # Calls display_info() method from Car
print(car.start_engine())  # Calls overridden start_engine() from Car
print(car.car_specific_info())

motorbike = Motorbike("Yamaha", "MT-07", 2021, "Sport Bike")
print(print_vehicle_info(motorbike))  # Calls display_info() method from Motorbike
print(motorbike.start_engine())  # Calls overridden start_engine() from Motorbike
print(motorbike.bike_specific_info())
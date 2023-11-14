class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

    def calculate_mileage(self, miles_driven, fuel_consumed):
        pass

    def calculate_capacity(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_efficiency):
        super().__init__(brand, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, miles_driven, fuel_consumed):
        if fuel_consumed > 0:
            mileage = miles_driven / fuel_consumed
            return f"Mileage: {mileage} miles per gallon"
        else:
            return "Invalid fuel consumption value, cannot calculate mileage."


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def calculate_mileage(self, miles_driven, fuel_consumed):
        if fuel_consumed > 0:
            mileage = miles_driven / fuel_consumed
            return f"Mileage: {mileage} miles per gallon"
        else:
            return "Invalid fuel consumption value, cannot calculate mileage."


class Truck(Vehicle):
    def __init__(self, brand, model, year, towing_capacity):
        super().__init__(brand, model, year)
        self.towing_capacity = towing_capacity

    def calculate_capacity(self):
        return self.towing_capacity


car = Car(brand="Golf", model="7", year=2013, fuel_efficiency=30)
motorcycle = Motorcycle(brand="Harley", model="Fatboy", year=2021)
truck = Truck(brand="Ford", model="Raptor", year=2023, towing_capacity=8000)

car.display_info()
print( car.calculate_mileage(5000,30))

motorcycle.display_info()
print( motorcycle.calculate_mileage(100,3))

truck.display_info()
print("Towing Capacity:", truck.calculate_capacity())

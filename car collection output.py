class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

# Car collection
cars = [
    Car("Toyota", "Camry", 2022),
    Car("Honda", "Civic", 2021),
    Car("Ford", "Mustang", 2023),
    Car("BMW", "X5", 2022),
]

# Output
print("Car Collection:")
print("-" * 40)
for i, car in enumerate(cars, 1):
    print(f"{i}. {car}")
print("-" * 40)
print(f"Total cars: {len(cars)}")
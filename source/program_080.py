class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


cars = [
    Car("Toyota", "Fortuner"),
    Car("Honda", "City"),
    Car("Tesla", "Model 3")
]

for car in cars:
    car.display()
    print()

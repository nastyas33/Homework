class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def switch_on(self):
        return ("Автомобиль заведен")

    def switch_off(self):
        return ("Автомобиль заглушен")

    def __str__(self):
        return f"The model of the car is {self.type}, year is {self.color}, and color is {self.color}"

Car1 = Car(color="white", type="Audi", year=2018)
Car2 = Car(color="black", type="BMW", year=2015)

print(f"{Car2.type}", Car2.switch_on())
print(f"{Car2.type}", Car2.switch_off())
print(Car1)
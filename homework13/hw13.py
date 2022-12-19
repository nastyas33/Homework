class Car:
    instanse_counter = 0

    def __init__(self, mileage: int, name: str, year: int, price: int):
        self.mileage = mileage
        self.name = name
        self.year = year
        self.price = price
        Car.instanse_counter += 1

    def __str__(self):
        return f"name: {self.name}, mileage: {self.mileage}, year: {self.year}, price: {self.price}$"

    def __eq__(self, other):
        if self.name == other.name and self.year == other.year:
            return True
        else:
            return False

    def price_in_BYN(self):
        return f"Price in USD is {self.price}. Price in BYN is {self.price * 2.53}"

    @classmethod
    def get_counter(cls):
        return Car.instanse_counter

    @staticmethod
    def made_in_country(brand):
        if brand == "BMW" or brand == "Mercedes" or brand == "Audi":
            return "The car was made in Germany"
        else:
            return "The car was made in another country"

    @property
    def miles(self):
        return self.mileage

    @miles.setter
    def miles(self, new_mileage_value):
        self.mileage = new_mileage_value

    @miles.deleter
    def miles(self, new_mileage_value):
        print("Mileage is null.")
        self.mileage = None

class Chevrolet(Car):
    instanse_counter = 0

    def made_in_country(brand):
        return "Usa"


car1 = Car(mileage=150_000, name="BMW", year=2012, price=40000 )
car2 = Car(mileage=28_000, name="Toyota", year=2020, price=77000)
car3 = Car(mileage=178_000, name="BMW", year=2012, price=38900)

print(Car.get_counter())

car_chevrolet = Chevrolet(1000, "Taho", 2001, 30_000)
print(Chevrolet.get_counter())


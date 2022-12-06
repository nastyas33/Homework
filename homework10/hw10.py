class Cosmetics:
    def __init__(self, brand, product, price):
        self.brand = brand
        self.product = product
        self.price = price

class CareCosmetics(Cosmetics):
    def __init__(self, brand, product, price, skin):
        Cosmetics.__init__(self, brand, product, price)
        self.skin = skin

    def __str__(self):
        return f"Product: {self.product} for {self.skin} skin, brand: {self.brand}, price: {self.price}"

    def Hello(self):
        return f"New product for {self.skin} skin was added"

class DecorativeCosmetics(Cosmetics):
    def __init__(self, brand, product, price, for_):
        Cosmetics.__init__(self, brand, product, price)
        self.for_ = for_

    def __str__(self):
        return f"Product: {self.product} for {self.for_}, brand: {self.brand}, price: {self.price}"

    def Hello(self):
        return f"New product for {self.for_} was added"

class Lips(DecorativeCosmetics):
    def __init__(self, brand, product, price, for_, type):
        DecorativeCosmetics.__init__(self, brand, product, price, for_)
        self.type = type

    def __str__(self):
        return f"Product: {self.product} - {self.type} for {self.for_}, brand: {self.brand}, price: {self.price}"

    def __call__(self, skin, type):
        self.type, self.skin = skin, type
        return

class ProfessionalCare(CareCosmetics):
    def __init__(self, brand, product, price, skin, age):
        CareCosmetics.__init__(self, brand, product, price, skin)
        self.age = age

    def __str__(self):
        return f"Product: {self.product}, brand: {self.brand}, price: {self.price}, for {self.skin} skin {self.age}"

    def Hello(self):
        return f"New product for age: {self.age} was added"

CareCosmetics_1=CareCosmetics(brand="Dior", product="Lotion1", price=150, skin="Normal")
DecorativeCosmetics_1=DecorativeCosmetics(brand="YSL", product="Pomade1", price=75, for_="lips")
Lips_1 = Lips(brand="YSL", product="Pomade1", price=75, for_="lips", type="pomade")
ProfessionalCare_1 = ProfessionalCare(brand="Dior", product="Lotion1", price=150, skin="Normal", age="20+")

print(CareCosmetics_1)
print(DecorativeCosmetics_1)
print(Lips_1)
print(ProfessionalCare_1)
print()
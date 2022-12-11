class Soda:
    def __init__(self, flavour):
        self.flavour = flavour

    def show_my_drink(self):
        if self.flavour == "-":
            return f"Обычная газировка"
        else:
            return f"Газировка и {self.flavour}"


soda1 = Soda("strawberry")
soda2 = Soda("-")
soda3 = Soda("mix")

print(soda1.show_my_drink())


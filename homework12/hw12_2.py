import dataclasses


class Soda:
    def __init__(self, addiction: str = None):
        self.addiction = addiction

    def show_my_drink(self):
        if self.addiction is None:
            return "Just soda"
        else:
            return f"Soda with {self.addiction}"

drink1 = Soda()
drink2 = Soda("Banan")

print(drink1.show_my_drink())
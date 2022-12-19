from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimetr_of_circle(self):
        __pi = pi
        return f"Perimetr = {2 * self.radius * __pi}"

    def square_of_circle(self):
        __pi = pi
        return f"Square = {self.radius ** 2 * __pi}"

circle1 = Circle(radius=7)

#print(circle1.perimetr_of_circle(), circle1.square_of_circle())

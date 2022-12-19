class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def perimetr_of_rectangle(self):
        return f"Perimetr = {2 * (self.side_a + self.side_b)}"

    def square_of_rectangle(self):
        return f"Square = {self.side_a * self.side_b}"

rectangle1 = Rectangle(side_a=3, side_b=9)

#print(rectangle1.perimetr_of_rectangle(), rectangle1.square_of_rectangle())

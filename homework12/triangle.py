class Triangle:
    def __init__(self, side_a, side_b, side_c, radius):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.radius = radius

    def perimetr_of_triangle(self):
        return f"Perimetr = {self.side_a + self.side_b + self.side_c}"

    def square_of_triangle(self):
        return f"Square = {self.side_a * self.side_b * self.side_c / 4 * self.radius}"

triangle1 = Triangle(side_a=5, side_b=4, side_c=10, radius=3)

#print(triangle1.perimetr_of_triangle(), triangle1.square_of_triangle())


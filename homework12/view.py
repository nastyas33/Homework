from triangle import Triangle
from circle import Circle
from rectangle import Rectangle

triangle1 = Triangle(side_a=5, side_b=4, side_c=10, radius=3)
circle1 = Circle(radius=7)
rectangle1 = Rectangle(side_a=3, side_b=9)


def print_results():
    return {"triangle": {"perimetr": triangle1.perimetr_of_triangle(), "square": triangle1.square_of_triangle()}}
           #{"circle": {"circle": circle1.perimetr_of_triangle(3), "square": circle1.square_of_triangle(4)}
           #{"rectangle": {"rectangle": rectangle1.perimetr_of_triangle(), "square": rectangle1.square_of_triangle()}}

print(print_results())
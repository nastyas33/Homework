from triangle import Triangle
from circle import Circle
from rectangle import Rectangle

triangle1 = Triangle(side_a=5, side_b=4, side_c=10, radius=3)
circle1 = Circle(radius=7)
rectangle1 = Rectangle(side_a=3, side_b=9)


def print_results():
    return f"Triangle: {triangle1.perimetr_of_triangle(), triangle1.square_of_triangle()}, " \
           f"Circle: {circle1.perimetr_of_circle(), circle1.square_of_circle()}" \
           f"Rectangle: {rectangle1.perimetr_of_rectangle(), rectangle1.square_of_rectangle()}"

print(print_results())
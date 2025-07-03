
class Shape:

    def area(self) -> float:
        return 0

    def perimeter(self) -> float:
        return 0

class Rectangle(Shape):

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius


if __name__ == "__main__":
    rectangle_1 = Rectangle(4, 5)
    rectangle_2 = Rectangle(3, 6)
    circle_1 = Circle(5)
    circle_2 = Circle(3)

    shapes = [rectangle_1, rectangle_2, circle_1, circle_2]

    for shape in shapes:
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")

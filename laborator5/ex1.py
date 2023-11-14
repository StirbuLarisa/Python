import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):

        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


circle = Circle(radius=5)
rectangle = Rectangle(length=4, width=6)
triangle = Triangle(side1=3, side2=4, side3=5)


print("cerc:")
print("arie:", circle.area())
print("perimetru:", circle.perimeter())
print()

print("dreptunghi:")
print("arie:", rectangle.area())
print("perimetru:", rectangle.perimeter())
print()

print("triunghi:")
print("arie:", triangle.area())
print("perimetru:", triangle.perimeter())
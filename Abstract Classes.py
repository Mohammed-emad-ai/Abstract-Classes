from abc import ABC, abstractmethod

class Shape(ABC):
    # Abstract method
    @abstractmethod
    def area(self):
        pass

    # Abstract method
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implementing abstract methods
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Cannot instantiate Shape (abstract class)
# s = Shape()  # Raises TypeError

# Instantiating Rectangle (concrete class)
r = Rectangle(10, 5)
print(f"Area: {r.area()}")  # Output: Area: 50
print(f"Perimeter: {r.perimeter()}")  # Output: Perimeter: 30

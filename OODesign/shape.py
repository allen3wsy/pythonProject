from abc import ABC, abstractmethod


class Shape(ABC):
    """An Abstract Base Class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculates the area of the shape. Must be implemented by subclasses."""
        pass  # Abstract methods often have an empty body in the base class

    def describe(self):
        """A concrete method inherited by all subclasses."""
        return f"This shape has an area of {self.area()}."


# This will raise a TypeError:
# shape = Shape()

class Circle(Shape):
    """A concrete class that must implement the area method."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Provides the specific implementation for a circle."""
        return 3.14 * self.radius * self.radius


class Square(Shape):
    """Another concrete class with a different implementation for area."""

    def __init__(self, side):
        self.side = side

    def area(self):
        """Provides the specific implementation for a square."""
        return self.side * self.side


# Now we can instantiate concrete classes
circle = Circle(5)
square = Square(4)

print(circle.describe())  # Output: This shape has an area of 78.5.
print(square.describe())  # Output: This shape has an area of 16.0.

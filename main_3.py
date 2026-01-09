class Circle:
    def __init__(self, radius):
        self._radius = radius # Conventionally, use a single underscore for a "protected" attribute

    @property
    def radius(self):
        """The getter method: Called when you access circle.radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """The setter method: Called when you assign a value, e.g., circle.radius = 10"""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

# Usage:
c = Circle(5)
print(c.radius)  # Calls the @property getter
c.radius = 10    # Calls the @radius.setter
print(c.radius)
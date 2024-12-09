class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle: length={self.length}, width={self.width}"

# Create a Rectangle object
new_rectangle1 = Rectangle(7, 3)
print(f"Area: {new_rectangle1.rectangle_area()}")

print(f"Perimeter: {new_rectangle1.perimeter()}")
print(new_rectangle1)

class Shape:
    def __init__(self, side_length, num_sides):
        self.side_length = side_length
        self.num_sides = num_sides

    def perimeter(self):
        return self.side_length * self.num_sides

    def area(self):
        import math
        return (self.num_sides * self.side_length**2) / (4 * math.tan(math.pi / self.num_sides))

# Example usage
shape = Shape(5, 4)  # Square with side length 5
print("Perimeter:", shape.perimeter())
print("Area:", shape.area())
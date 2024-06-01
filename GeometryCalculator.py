import math

class GeometryCalculator:

    def calculate_rectangle_area(self, length, width):
        return length * width
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2


if __name__ == "__main__":
    calculator = GeometryCalculator()

# TODO: Implement the feature to calculate the area of a circle
# TODO: Implement the feature to calculate the area of a rectangle # length = 10
width = 6
length = 10
print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")
radius = 5
print(f"The area of the circle with radius {radius} ={calculator.calculate_circle_area(radius)}")

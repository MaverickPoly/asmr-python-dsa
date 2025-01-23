import math


class Rectangle:
    def __init__(self, bottom_left, top_right):
        x1, y1 = bottom_left
        x2, y2 = top_right
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Invalid rectangle: bottom_left must be below and to the left of top_left")

        self.bottom_left = bottom_left
        self.top_right = top_right

    def width(self):
        return self.top_right[0] - self.bottom_left[0]

    def height(self):
        return self.top_right[1] - self.bottom_left[1]

    def area(self):
        return self.width() * self.height()

    def perimeter(self):
        return 2 * self.width() * self.height()

    def diagonal(self):
        return math.sqrt(self.width() ** 2 + self.height() ** 2)

    def contains_point(self, point):
        x, y = point
        x1, y1 = self.bottom_left
        x2, y2 = self.top_right
        return x1 <= x <= x2 and y1 <= y <= y2

    def __repr__(self):
        return f"Rectangle(bottom_left={self.bottom_left}, top_right={self.top_right})"


if __name__ == '__main__':
    rect = Rectangle((0, 0), (4, 3))

    print(rect)

    print(f"Width: {rect.width()}")
    print(f"Height: {rect.height()}")

    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")
    print(f"Diagonal length: {rect.diagonal()}")
    point_inside = (2, 2)
    point_outside = (5, 5)
    print(f"Does the rectangle contain {point_inside}? {rect.contains_point(point_inside)}")
    print(f"Does the rectangle contain {point_outside}? {rect.contains_point(point_outside)}")


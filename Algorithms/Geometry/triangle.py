import math
from vector2 import Vector2


class Triangle:
    def __init__(self, vertex1, vertex2, vertex3):
        """Each vertex is a Vector2"""
        self.vertex1: Vector2 = Vector2(vertex1[0], vertex1[1])
        self.vertex2: Vector2 = Vector2(vertex2[0], vertex2[1])
        self.vertex3: Vector2 = Vector2(vertex3[0], vertex3[1])

    def perimeter(self):
        side1 = self._distance(self.vertex1, self.vertex2)
        side2 = self._distance(self.vertex2, self.vertex3)
        side3 = self._distance(self.vertex1, self.vertex3)
        return side1 + side2 + side3

    def area(self):
        """
        Calculates an area of the triangle
        """
        x1, y1 = self.vertex1.x, self.vertex1.y
        x2, y2 = self.vertex2.x, self.vertex2.y
        x3, y3 = self.vertex3.x, self.vertex3.y
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

    def contains_point(self, point: tuple[int, int]):
        x, y = point
        x1, y1 = self.vertex1.x, self.vertex1.y
        x2, y2 = self.vertex2.x, self.vertex2.y
        x3, y3 = self.vertex3.x, self.vertex3.y

        area_total = self.area()
        area1 = abs((x * (y2 - y3) + x2 * (y3 - y) + x3 * (y - y2)) / 2)
        area2 = abs((x1 * (y - y3) + x * (y3 - y1) + x3 * (y1 - y)) / 2)
        area3 = abs((x1 * (y2 - y) + x2 * (y - y1) + x * (y1 - y2)) / 2)

        return math.isclose(area1 + area2 + area3, area_total)

    @staticmethod
    def _distance(point1: Vector2, point2: Vector2):
        """
        plain distance:
          sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        """
        return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

    def __repr__(self):
        return f"Triangle({self.vertex1}, {self.vertex2}, {self.vertex3})"


if __name__ == '__main__':
    triangle = Triangle((0, 0), (4, 0), (0, 3))
    print(triangle)
    print(f"Perimeter: {triangle.perimeter()}")
    print("Area: {}".format(triangle.area()))

    point_inside = (1, 1)
    point_outside = (5, 5)
    print(f"Does the triangle contain {point_inside}? {triangle.contains_point(point_inside)}")
    print(f"Does the triangle contain {point_outside}? {triangle.contains_point(point_outside)}")

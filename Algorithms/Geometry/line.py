import math


class Line:
    def __init__(self, point1, point2):
        """
        Each point is a tuple of (x, y) coordinates
        """
        if point1 == point2:
            raise ValueError("A line must be defined by two distinct points!")
        self.point1 = point1
        self.point2 = point2

    def slope(self):
        """Calculate the slope"""
        x1, y1 = self.point1
        x2, y2 = self.point2
        if x2 - x1 == 0:
            return float("inf")
        return (y2 - y1) / (x2 - x1)

    def length(self):
        """Calculate the length of the line"""
        return self._distance(self.point1, self.point2)

    def midpoint(self):
        """Calculate the middle point of the line"""
        x1, y1 = self.point1
        x2, y2 = self.point2
        return (x1 + x2) / 2, (y1 + y2) / 2


    def contains_point(self, point):
        """Point lies on the line or not?"""
        x, y = point
        x1, y1 = self.point1
        x2, y2 = self.point2
        if x1 == x2:
            return math.isclose(x, x1)

        slope_to_point = (y - y1) / (x - x1) if x != x1 else float("inf")
        return math.isclose(slope_to_point, self.slope())

    def equation(self):
        """Get the math equation for the line: y = kx + c"""
        x1, y1 = self.point1
        k = self.slope()
        if k == float("inf"):
            return f"x = {x1}"
        c = y1 - k * x1
        return f"y = {k}x + {c}"

    @staticmethod
    def _distance(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def __repr__(self):
        return f"Line({self.point1}, {self.point2})"


if __name__ == '__main__':
    line = Line((0, 1), (4, 5))
    print(line)
    print("Slope: %f" % line.slope())
    print("Length: {}".format(line.length()))
    print(f"Mid Point: {line.midpoint()}")
    print("Equation:", line.equation())

    point_on_line = (2, 3)
    point_off_line = (3, 2)
    print(f"Does the line contain {point_on_line}? {line.contains_point(point_on_line)}")
    print(f"Does the line contain {point_off_line}? {line.contains_point(point_off_line)}")

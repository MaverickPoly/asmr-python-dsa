class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif isinstance(other, int):
            return Vector2(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif isinstance(other, int):
            return Vector2(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Vector2(self.x * other, self.y * other)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __eq__(self, other):
        if isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __iadd__(self, other):
        print(f"Other: {other}")
        if isinstance(other, Vector2):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, int):
            self.x += other
            self.y += other
        return self

    def __isub__(self, other):
        if isinstance(other, Vector2):
            self.x -= other.x
            self.y -= other.y
        elif isinstance(other, int):
            self.x -= other
            self.y -= other
        return self

    def __imul__(self, other):
        if isinstance(other, Vector2):
            self.x *= other.x
            self.y *= other.y
        elif isinstance(other, int):
            self.x *= other
            self.y *= other
        return self


if __name__ == '__main__':
    vector1 = Vector2(3, 4)
    vector2 = Vector2(1, 2)

    print("Vector1: ", vector1)
    print("Vector2: ", vector2)

    vector3 = vector1 + vector2
    print(f"Vector1 + Vector2 = {vector3}")

    vector4 = vector1 + 5
    print(f"Vector1 + 5 = {vector4}")

    vector5 = vector1 - vector2
    print(f"Vector1 - Vector2 = {vector5}")

    vector6 = vector1 - 3
    print(f"Vector1 - 3 = {vector6}")

    vector7 = vector1 * vector2
    print(f"Vector1 * Vector2 = {vector7}")

    vector8 = vector1 * 2
    print(f"Vector1 * 2 = {vector8}")

    print(f"Vector1 == Vector2: {vector1 == vector2}")
    print(f"Vector1 != Vector2: {vector1 != vector2}")
    print(f"Vector1 != Vector1: {vector1 != vector1}")
    print(f"Vector1 == Vector2 + Vector3: {vector1 == (vector2+ vector3)}")

    print()
    print(f"bool(Vector1): {bool(vector1)}")
    print(f"Vector2(0, 0): {bool(Vector2())}")

    print("\n--------------------")
    print(f"Vector1: {vector1}")
    print(f"Vector2: {vector2}")
    vector1 += vector2
    print(f"Vector1 After Vector1 += Vector2:", vector1)

    vector1 += 5
    print(f"Vector1 After Vector1 += 5:", vector1)

    vector1 -= vector2
    print(f"Vector1 After Vector1 -= Vector2:", vector1)

    vector1 -= 2
    print(f"Vector1 After Vector1 -= 2:", vector1)

    vector1 *= vector2
    print(f"Vector1 After Vector1 *= Vector2:", vector1)

    vector1 *= 3
    print(f"Vector1 After Vector1 *= 3:", vector1)

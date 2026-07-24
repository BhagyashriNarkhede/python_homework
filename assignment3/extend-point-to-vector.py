import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        x_difference = self.x - other.x
        y_difference = self.y - other.y

        distance = math.sqrt(
            x_difference ** 2 + y_difference ** 2
            )

        return distance

class Vector(Point):

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # Override + operator
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y

        return Vector(new_x, new_y)
        

point1 = Point(2, 3)
point2 = Point(2, 3)
point3 = Point(5, 7)

print(point1)
print(point3)

print(point1 == point2)
print(point1 == point3)

print(point1.distance(point3))

vector1 = Vector(1, 2)
vector2 = Vector(3, 4)

print(vector1)
print(vector2)

vector3 = vector1 + vector2

print(vector3)
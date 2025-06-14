import copy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


a = Point(1, 2)
b = a
c = Point(1, 2)
print(a is c)
print(a == c)
print(a is b)
print(a == b)

print(copy.copy(a) == a)
print(copy.deepcopy(a) == a)
print(copy.deepcopy(a) is a)
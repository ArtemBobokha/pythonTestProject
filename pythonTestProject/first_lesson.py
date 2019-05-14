import sys


class Point:
    def __init__(self, x, y=1):
        self.x = x
        self.y = y


p = Point(0, 0)

print('dir(Point):{}'.format(dir(Point)))
print('dir(p):{}'.format(dir(p)))

print(sys.getrefcount(p))
print(sys.getsizeof(p))

print(type(p))

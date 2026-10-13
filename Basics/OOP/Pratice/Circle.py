"""
Don't generate lab for this module
"""
import math

class Circle:
    def __init__(self, r):
        self.redius = r

    @property
    def redius(self):
        return self._redius

    @redius.setter
    def redius(self, r):
        self._redius = math.fabs(r)

    def func_area(self):
        return math.pi * (self.redius ** 2)

    def fun_perimeter(self):
        return math.pi * 2 * self.redius

circle = Circle(5.0)
print(circle.func_area())
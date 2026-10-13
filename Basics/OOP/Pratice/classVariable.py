from venv import logger


class Rectangle:
    count = 0

    def __init__(self, length = 1, breadth = 1):
        self.length = length
        self.breadth = breadth
        Rectangle.count += 1

    def func_area(self):
        return self.length * self.breadth

    def func_perimeter(self):
        return 2 * (self.length + self.breadth)

    def func_instance_getCount(cls):
        return cls.count

    @classmethod
    def func_static_getCount(cls):
        return cls.count

r1 = Rectangle(5,10)
print(r1.func_area())
print(r1.func_perimeter())
print(r1.func_instance_getCount())

"""
50
30
1
"""

r2 = Rectangle(6,10)
print(r2.func_area())
print(r2.func_perimeter())
print(r2.func_instance_getCount())
"""
50
30
1
60
32
2
"""

print(r1.func_instance_getCount())
print(r2.func_instance_getCount())
"""
2
2
"""

try:
    print(Rectangle.func_instance_getCount())
except Exception as e:
    logger.exception(e)

"""
Rectangle.func_instance_getCount() missing 1 required positional argument: 'cls'
Traceback (most recent call last):
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/OOP/Pratice/classVariable.py", line 57, in <module>
    print(Rectangle.func_instance_getCount())
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
TypeError: Rectangle.func_instance_getCount() missing 1 required positional argument: 'cls'
"""

print(Rectangle.func_static_getCount())
"""
2
"""

"""
**Class Methods:
1. Declared outside of the class
2. Created only once and can be used multiple times
3. Can be accessed using object.
4. Can also be accessed through the class name, but needs to decorated with @classmethod.
5. Purpose of this method is to give class level meta data or shareable data betweeen the objects.
6. These are also called as static variables.
"""
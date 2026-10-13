from venv import logger


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def func_area(length, breadth):
        return length * breadth

    @staticmethod
    def func_static_area(length, breadth):
        return length * breadth

"""
    @staticmethod
    def func_static_area():
        return self.length * self.breadth
        
    We cannot use instance variables inside the static method.
"""


r = Rectangle(5,10)

try:
    print(r.func_area(5,10))
except Exception as e:
    logger.exception(e)

"""
Rectangle.func_area() takes 2 positional arguments but 3 were given
Traceback (most recent call last):
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/OOP/Pratice/staticMethod.py", line 20, in <module>
    print(r.func_area(5,10))
          ~~~~~~~~~~~^^^^^^
TypeError: Rectangle.func_area() takes 2 positional arguments but 3 were given 
 
 At line 20, we are passing r (as reference variable and then length as 5 and breadth as 10), 
 but line 9 takes 
    length variable as reference and take r
    breadth variable takes 5
    and no variable to accept 10 and hence this error
"""

try:
    print(Rectangle.func_area(5,10))
except Exception as e:
    logger.exception(e)

"""
50
"""

try:
    print(r.func_static_area(5,10))
except Exception as e:
    logger.exception(e)

"""
50
"""

try:
    print(Rectangle.func_static_area(5,10))
except Exception as e:
    logger.exception(e)

"""
50
"""
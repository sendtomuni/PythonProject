class Rectangle:
    def __init__(self, length, breadth):
        self.set_length(length)
        self.breadth = breadth

    def set_length(self, length):
        if length > 0:
            self.length = length
        else:
            self.length = 1

    def get_length(self):
        return self.length


r = Rectangle(5,10)
print(r.get_length())

"""
5
"""

r.length = -10
print(r.get_length())

"""
5
-10

Class has a validator, but as the variable is exposed to outside and hence users directly making an stale update
"""

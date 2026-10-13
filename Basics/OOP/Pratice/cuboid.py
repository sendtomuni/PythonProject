class Rectangle:

    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def func_get_area(self):
        return self.length * self.breadth

    def func_get_perimeter(self):
        return 2 * (self.length + self.breadth)

class Cuboid(Rectangle):
    def __init__(self, l, b, h):
        self.height = h
        super().__init__(l,b) # This is mandatory to invoke the Rectangle class

    def func_get_volume(self):
        return self.height * self.length * self.breadth

cuboid = Cuboid(5,10,20)
print(cuboid.func_get_volume())
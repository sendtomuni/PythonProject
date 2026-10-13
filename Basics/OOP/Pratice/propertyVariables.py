

class Rectangle:
    def __init__(self, length, breadth):
        self._length = length
        self._breadth = breadth

    @property
    def length(self):
        return self._length

    """
    A class body runs from top to bottom when Python first defines the class, just like an ordinary script. 
    Each def creates a function and each decorator is applied straight away. 
    A decorator line such as @name.setter is an expression: 
        Python has to look up name in the class body that is still being built before it can call .setter on it. 
        That name only exists once the @property-decorated getter has run. 
        @property turns the getter into a property object and binds it to name, 
        and .setter is a method of that object. 
        It returns a new property that keeps the getter and adds the setter, 
        and that new property is bound back to the same name. 
        So the getter must always come first. 
        
        If the .setter (or .deleter) line comes earlier, 
        the name is not defined yet. 
        Python then raises NameError while the class is being defined, 
        before any object is created and before any line after the class runs. 
        The same rule applies to .deleter: getter first, then setter and deleter, all with the same function name.
    """
    @length.setter
    def length(self, length):
        if length > 0:
            self._length = length
        else:
            self._length = 1

r = Rectangle(5,10)
print(r.length)
r.length = -9
print(r.length)
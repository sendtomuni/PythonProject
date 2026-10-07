import math
"""
If a function is declared as an object, then we call that as a first-class function.
"""

print(print.__name__)

## Every function is an object and those object has their own attributes like __name__

def totalArea(l, b, h): # outer Function
    def area(l, b): # inner function
        a = l * b
        return  a
    return 2 * (area(l,b) + area(b,h) + area(l,h))

total = totalArea(5,10,2)
print(total)

# inner function can only call by the outer function
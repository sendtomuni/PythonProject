"""
Simple
"""
class Parent_1:
    pass
class Child_1(Parent_1):
    pass
print(Child_1.mro())
"""
[
    <class '__main__.Child_1'>, 
    <class '__main__.Parent_1'>, 
    <class 'object'>
]
"""
"""
MultiLevel
"""
class GrandParent1:
    pass
class Parent2(GrandParent1):
    pass
class Child2(Parent2):
    pass
print(Child2.mro())
"""
[
    <class '__main__.Child2'>, 
    <class '__main__.Parent2'>, 
        <class '__main__.GrandParent1'>, 
    <class 'object'>
]
"""

"""
Multiple
"""
class Parent3:
    pass
class Parent4:
    pass
class Child3(Parent3, Parent4):
    pass
print(Child3.mro())
"""
[
    <class '__main__.Child3'>, 
    <class '__main__.Parent3'>, 
    <class '__main__.Parent4'>, 
    <class 'object'>
]
"""

"""
Mixed
"""
class Grandparent2:
    pass
class GrandParent3:
    pass
class Parent5(Grandparent2):
    pass
class Parent6(GrandParent3):
    pass
class Child4(Parent5, Parent6):
    pass
print(Child4.mro())
"""
[
    <class '__main__.Child4'>, 
    <class '__main__.Parent5'>, 
        <class '__main__.Grandparent2'>, 
    <class '__main__.Parent6'>, 
        <class '__main__.GrandParent3'>, 
    <class 'object'>
]
"""
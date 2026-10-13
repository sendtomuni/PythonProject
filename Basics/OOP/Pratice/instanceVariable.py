from logging import log
from venv import logger


class Test:
    def __init__(self):
        self.a = 10;

    def func(self):
        self.b = 20;

    def show(self):
        print(f'a = {self.a}')
        print(f'b = {self.b}')
        print(f'c = {self.c}')

try:
    t1 = Test()
    t1.show();
except Exception as e:
    logger.exception(e)
"""
a = 10
Traceback (most recent call last):
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/OOP/Pratice/instanceVariable.py", line 15, in <module>
    t1.show();
    ~~~~~~~^^
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/OOP/Pratice/instanceVariable.py", line 10, in show
    print(f'b = {self.b}')
                 ^^^^^^
AttributeError: 'Test' object has no attribute 'b'
"""
try:
    t2 = Test()
    t2.func()
    t2.show()
except Exception as e:
    logger.exception(e)
"""
a = 10
b = 20
Traceback (most recent call last):
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/OOP/Pratice/instanceVariable.py", line 30, in <module>
    t2.show()
    ~~~~~~~^^
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/OOP/Pratice/instanceVariable.py", line 11, in show
    print(f'c = {self.c}')
                 ^^^^^^
AttributeError: 'Test' object has no attribute 'c'
"""
try:
    t3 = Test()
    t3.func()
    t3.c = 30
    t3.show()
except Exception as e:
    logger.exception(e)
"""
a = 10
b = 20
c = 30
"""


"""
**Instance Methods:
1. Declared inside of __init__ or any other method
2. Can also be declared through the object.
3. While created through the __init__ method, it gets defined and initialized on object creation.
4. If it declared through other instance methods, instance method invocation is mandatory to created and initialize.
5. If it declared through object variable then we can use it, but it has to defined correctly. 
6. Variable value is specific to that particular instance and re-initializes in every instance creation.
"""
from venv import logger


class Parent:
    def __init__(self, pri, pro, pub):
        self.public_variable = pub
        self._protected_variable = pro
        self.__private_variable = pri

    def func_show_variables(self):
        print(f'Public variable : {self.public_variable}')
        print(f'Protected Variable {self._protected_variable}')
        print(f'Private Variable {self.__private_variable}')

class Child(Parent):
    def __init__(self, pri, pro, pub):
        super().__init__(pri, pro, pub)

    def func_display_variables(self):
        print(f'Public variable : {self.public_variable}')
        print(f'Protected Variable {self._protected_variable}')
        print(f'Private Variable {self.__private_variable}')

child = Child(5,10,15)
child.func_show_variables()

"""
Public variable : 15
Protected Variable 10
Private Variable 5
"""
try:
    child.func_display_variables()
except Exception as e:
    logger.exception(e)
"""
Public variable : 15
Protected Variable 10
Traceback (most recent call last):
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/OOP/Pratice/dataHiding.py", line 27, in <module>
    child.func_display_variables()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/OOP/Pratice/dataHiding.py", line 19, in func_display_variables
    print(f'Private Variable {self.__private_variable}')
                              ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Child' object has no attribute '_Child__private_variable'. Did you mean: '_Parent__private_variable'?
"""

child.public_variable = 105
child._protected_variable = 110
child.__private_variable = 115 # A different variable with name __private_variable

child.func_show_variables()
"""
Public variable : 105
Protected Variable 110
Private Variable 5
"""

child._Parent__private_variable = 115 # Name Mangling
child.func_show_variables()
"""
Public variable : 105
Protected Variable 110
Private Variable 115
"""

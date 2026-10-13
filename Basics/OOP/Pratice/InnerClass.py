from venv import logger


class Outer:
    def __init__(self):
        self.in_obj = self.Inner()

    def func_display(self):
        self.in_obj.func_show()

    class Inner:
        def __init__(self):
            self.idata = 'Inner class'

        def func_show(self):
            print(self.idata)

outer = Outer()
outer.func_display()
try:
    outer.func_show()
except Exception as e:
    logger.exception(e)

"""
Inner class
Traceback (most recent call last):
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/OOP/Pratice/InnerClass.py", line 18, in <module>
    outer.func_show()
    ^^^^^^^^^^^^^^^
AttributeError: 'Outer' object has no attribute 'func_show'
"""

outer.in_obj.func_show()
"""
Inner class
"""
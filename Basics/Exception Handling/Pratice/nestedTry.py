from venv import logger

L = [10,20,30,40,50]

def fun_without_valueError():
    try:
        try:
            index = int(input('Enter Index'))
        except ValueError as e:
            logger.exception(e)
        print(L[index])
    except IndexError as e:
        logger.exception(e)

"""
For fun_without_valueError with input abc
/Users/subarnasekharmuni/PycharmProjects/PythonProject/.venv/bin/python /Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/Exception Handling/Pratice/nestedTry.py 
Enter Indexabc
invalid literal for int() with base 10: 'abc'
Traceback (most recent call last):
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/Exception Handling/Pratice/nestedTry.py", line 7, in <module>
    index = int(input('Enter Index'))
ValueError: invalid literal for int() with base 10: 'abc'
Traceback (most recent call last):
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/Exception Handling/Pratice/nestedTry.py", line 10, in <module>
    print(L[index])
            ^^^^^
NameError: name 'index' is not defined

Process finished with exit code 1
"""
def fun_with_valueError():
    try:
        try:
            index = int(input('Enter Index'))
        except ValueError as e:
            logger.exception(e)
        print(L[index])
    except IndexError as e:
        logger.exception(e)
    except NameError as e:
        logger.exception(e)

"""
For fun_with_valueError index abc, process will terminate with 0
Enter Indexabc
invalid literal for int() with base 10: 'abc'
Traceback (most recent call last):
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/Exception Handling/Pratice/nestedTry.py", line 36, in <module>
    index = int(input('Enter Index'))
ValueError: invalid literal for int() with base 10: 'abc'
name 'index' is not defined
Traceback (most recent call last):
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/Exception Handling/Pratice/nestedTry.py", line 39, in <module>
    print(L[index])
            ^^^^^
NameError: name 'index' is not defined

Process finished with exit code 0
"""

fun_with_valueError()
fun_without_valueError()
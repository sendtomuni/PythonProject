from venv import logger


def fun_writeToExistingFile(fileName):
    file = open(fileName, 'x')
    str = 'Writing Version 2'
    file.write(str)
    file.close()

try:
    fun_writeToExistingFile('overwrite.txt')
except Exception as e:
    logger.exception(e) # Exception
    """
    [Errno 17] File exists: 'overwrite.txt'
Traceback (most recent call last):
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/File Handling/Pratice/writingToNewFileOnly.py", line 11, in <module>
    fun_writeToExistingFile('overwrite.txt')
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/Users/subarnasekharmuni/PycharmProjects/PythonProject/Basics/File Handling/Pratice/writingToNewFileOnly.py", line 5, in fun_writeToExistingFile
    file = open(fileName, 'x')
FileExistsError: [Errno 17] File exists: 'overwrite.txt'
    """
else:
    print('File written Successfully')

try:
    fun_writeToExistingFile('newWrite.txt') #Successful
except Exception as e:
    logger.exception(e)
else:
    print('File written Successfully')
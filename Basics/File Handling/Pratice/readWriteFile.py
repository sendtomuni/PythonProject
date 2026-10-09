fileName = 'my.dat'
#
# def fun_readAndWrite():
#     file = open(fileName, 'r+')
#     data = file.read()
#     print(data) # ABCDEF
#     str = '123'
#     file.write(str) # Here 123 will write after ABCDEF, because while reading file cursor has already been moved to end of F
#     file.close()
#
# fun_readAndWrite()
#
#
# def fun_WriteAndRead():
#     file = open(fileName, 'w+')
#     str = '456'
#     file.write(str) # Here file will overwrite 456 with ABCDEF123, as cursor is on beginning
#
#     data = file.read() # Data will be empty though file has 456, because wfter werite cursor has move to position after 6
#     print(data)
#     file.close()
#
# fun_WriteAndRead()
#
#
# def fun_WriteAndReadFromBeginning():
#     file = open(fileName, 'w+')
#     str = '789'
#     file.write(str) # Here file will overwrite 789 with 456, as cursor is on beginning
#
#     file.seek(0,0) # moving cursor back to beginning
#     data = file.read() # Data will read 789
#     print(data) # 789
#     file.close()
#
# fun_WriteAndReadFromBeginning()
#

def fun_WriteAndReadInDifferentOrder():
    file = open(fileName, 'w+')
    data = file.read()
    print(data) # Read empty
    # Reason code didn't read anything (and why this print(data) output is blank) comes down to how the 'w+' mode works in Python.
    # When we open a file with open(fileName, 'w+'), Python does two things immediately:
    # 1. Truncates the file: It completely erases any existing content inside the file (the "789" is wiped out the millisecond open() is executed).
    # 2. Positions the cursor: It places the file cursor at the very beginning (position 0) of a now-empty file.
    # Because the file was wiped clean by the 'w+' flag, when you call file.read(), there is absolutely nothing left to read. Hence, data is empty, and nothing prints.

    str = '10 11 12'
    file.write(str) # Here file will overwrite 10 11 12 with 789, as cursor is on beginning

    file.close()

fun_WriteAndReadInDifferentOrder()

"""
Summary Checklist of + Modes

Mode	        Reads?	Writes?	           Truncates (wipes) file on open?	     Fails if file doesn't exist?
'r+' (or '+r')	Yes	     Yes	           ❌ No	                             Yes (FileNotFoundError)
'w+' (or '+w')	Yes	     Yes	           Yes (Wipes everything instantly)	     ❌ No (Creates a new file)
'a+' (or '+a')	Yes	     Yes	           ❌ No	                             ❌ No (Appends to end)
"""
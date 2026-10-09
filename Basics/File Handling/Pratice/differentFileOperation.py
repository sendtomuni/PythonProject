fileName = 'Data1.txt'

def fun_read_with_characher(file):
    data = file.read(10)
    print(data)

def fun_read_line(file):
    data = file.readline()
    print(data)

def fun_read_lines(file):
    data = file.readlines()
    print(data)

def fun_intializeFile(func, mode):
    file = open(fileName,mode)
    def fun_closeFilse():
        nonlocal file
        print(f'closing file: {file.name}')
        file.close()
    return file, fun_closeFilse

oper = fun_intializeFile(fun_read_with_characher, 'r')
fun_read_with_characher(oper[0])
print('*'* 15)
fun_read_with_characher(oper[0])
print('*'* 15)
fun_read_with_characher(oper[0])
print('*'* 15)
fun_read_with_characher(oper[0])
print('*'* 15)
fun_read_with_characher(oper[0])
print('*'* 15)
oper[1]()


oper = fun_intializeFile(fun_read_with_characher, 'r')
fun_read_line(oper[0])
print('*'* 15)
fun_read_line(oper[0])
print('*'* 15)
fun_read_line(oper[0])
print('*'* 15)
fun_read_line(oper[0])
print('*'* 15)
fun_read_line(oper[0])
print('*'* 15)
fun_read_line(oper[0])
print('*'* 15)
fun_read_line(oper[0])
print('*'* 15)
fun_read_line(oper[0])
print('*'* 15)
oper[1]()

print('=' * 20)
oper = fun_intializeFile(fun_read_with_characher, 'r')
fun_read_lines(oper[0])
print('*'* 15)
oper[1]()

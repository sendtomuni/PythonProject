def fun_airthmatic(funName):
    return funName

def add(a, b):
    return a+b

def sum(a, b):
    return a-b

print(fun_airthmatic(add)(5,6))

## Let's make one outer and inner example
def fun_outer():
    print("Outer")
    def fun_inner():
        print("inner")
    return fun_inner

fun = fun_outer()
print("calling inner")
fun()
"""
Decorator function is a combination of closure function with taking the parameter as function
"""

def fun_outer(fun_display_fun):
    def fun_inner():
        print('*' * 10)
        fun_display_fun()
        print('*' * 10)
    return fun_inner

def fun_display():
    print("Hello")

f = fun_outer(fun_display)
f()

print()
print("=" * 20)
print()

def fun_display2():
    print("Hello2")

fun_display2() ## prints as declared
fun_display2 = fun_outer(fun_display2)  ## fun_display2 is decorated.
fun_display2()

print()
print("=" * 20)
print()

@fun_outer #Decorating with fun_outer function
def fun_display3():
    print("Hello3")

fun_display3()
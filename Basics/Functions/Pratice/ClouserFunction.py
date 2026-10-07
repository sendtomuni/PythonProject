"""
A function is called closure function if:
1. It has a nested function
2. It is returning a function
3. Inner function uses the variables from outer function
"""
msg ="hello"
def fun_outer(name):
    msg = "Welcome"
    def fun_inner():
        print('*' * 10)
        print(f"{msg} {name}")
        print("*" * 10)
    return fun_inner

f = fun_outer('Chinku')
f()

# changing the value of outer value.

def fun_get_counter():
    count = 0;
    def fun_increment_counter():
        nonlocal  count
        count += 1
        return count
    return fun_increment_counter

c1 = fun_get_counter()
c2 = fun_get_counter()
print(c1(), c1(), c1())
print(c2(), c2(), c2())
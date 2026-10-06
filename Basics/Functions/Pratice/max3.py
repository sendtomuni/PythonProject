# WAP to find maximum of 3 numbers using function. a 3 values to the function has to be positional

def func_max_finder(a, b, c, /):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

max = func_max_finder(5, 20, 15)
print(max)
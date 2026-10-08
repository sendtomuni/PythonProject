from venv import logger


def fun_div(a,b):
    if b != 0:
        c = a / b
        return c
    else:
        raise ZeroDivisionError


try:
    c = fun_div(10,2)
    print(c)
    c = fun_div(10,0)
except Exception as msg:
    logger.exception(msg)

print('End of Program')
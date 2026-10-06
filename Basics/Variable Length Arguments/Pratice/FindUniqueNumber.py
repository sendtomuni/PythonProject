def fun_unique_number(*args):
    unique_numbers = set(args)
    return list(unique_numbers)

print(fun_unique_number(1, 2, 3, 4, 5, 1, 2, 3, 6, 7))
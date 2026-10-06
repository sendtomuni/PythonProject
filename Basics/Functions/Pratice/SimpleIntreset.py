## SImple interest formula is given by SI = (P * R * T) / 100, but parameters has to be key word only

def func_simple_interest(*, P, R, T):
    return (P * R * T) / 100

SI = func_simple_interest(P=1000, R=5, T=2)
print(SI)
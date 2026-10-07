"""
These are the anonymous, simple and single lined functions.
Lambda functions are useful in Functional programming
"""

def double(x):
    return x * 2

k = lambda x : x * 2

print(double(3))
print(k(3))
print()

l = lambda x,y : x+y

print(l(5,6))
print((lambda x,y : x +y)(5,6))

l1 = [1,2,3,4,5,6,7,8,9,10]

print()
f = list(filter(lambda x : x%2==0, l1))
print(f)
print(
    list(
        map(lambda x : -x, l1)
    )
)

print(
    list(
        map(
            lambda x : x if x%2 == 0 else -x
            , l1
        )
    )
)
print()

l2 = [[4,1, 'Five'], [2,2, 'Four'], [3,3,'Six']]
print(
    sorted(l2)
)

print(
    sorted(l2, key=lambda x : x[0] + x[1])
)

print(
    sorted(l2, key=lambda x : x[2])
)
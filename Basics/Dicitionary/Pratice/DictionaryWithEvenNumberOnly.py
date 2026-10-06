l1 = [(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR')]

d1 = {x:y for x,y in l1 if x%2 == 0}

print(d1)


## List Comprehensions:
l1 = {'Om', 'Amit', 'Subarna', 'Adwait'}

d2 = {x:y for x,y in enumerate(l1) if len(y) > 4}

print(l1, type(l1))

print(d2, type(d2))
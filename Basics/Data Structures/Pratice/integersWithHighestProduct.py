"""
claude:
Don't create lab for this
"""

import array

items = array.array('i', [0,-1,-3,-5,-8,2,4])

def highest_product(items):
    items = sorted(items)
    mul_large_2_item = items[len(items) - 1] * items[len(items) - 2]
    mul_least_2_item = items[0] * items[1]
    if mul_large_2_item> mul_least_2_item:
        return items[len(items) - 1], items[len(items) - 2]
    else:
        return items[0], items[1]

print(highest_product(items))
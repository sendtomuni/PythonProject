"""
claude:
Don't create lab for this
"""

unique_item = set()

items = [10,20,13,14,15,13,17,10,20,13]

def first_duplicate(items):
    for item in items:
        if item in unique_item:
            return item
        else:
            unique_item.add(item)
    else:
        return -1

item = first_duplicate(items)
print("First Duplicate ", item)
"""
claude:
Don't create lab for this
"""
from collections import Counter

inventory = {'apple':50, 'mango':100, 'banana':120, 'orange':70}

inventory_counter = Counter(inventory)

order_counter = Counter(apple=10, banana=12, orange=5)

inventory_counter.subtract(order_counter)

print(inventory_counter)
"""
claude:
Don't create lab for this
"""

from collections import deque

customers = deque(['john', 'james', 'mark', 'smith'])

def walk_in(customer):
    customers.append(customer)

def serviced():
    serviced_customer = customers.popleft()
    print("serviced customer", serviced_customer)
    return serviced_customer

serviced()
serviced()
walk_in('chinku')
print(customers)

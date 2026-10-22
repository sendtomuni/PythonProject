"""
claude:
Don't create lab for this
"""

inventory = {'soap':50, 'toothpaste':25, 'Shampoo':45.50, 'ToothBrush':15.99}


order = {'soap':5, "toothpaste":1, "Shampoo":2, "ToothBrush":3}

print(f"{'Product' :<13} : {'Price':<6}  {'Quantity':<10}  {'Sub Totals'}")
total = 0
for key,value in order.items():
    print(f"{key:<13} : {inventory.get(key):<6} X {value:<10} = {inventory[key] * value}")
    total += inventory[key] * value

print(f"{'Total Value is:' :<35} = {total}")

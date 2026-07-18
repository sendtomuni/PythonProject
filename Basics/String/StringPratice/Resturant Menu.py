totalItems = int(input("total items"))

items = []
itemPrices = []

for i in range(totalItems):
    items.append(input("Enter the name of the item: "))
    itemPrices.append(input("Enter the price of the item: "))

for i in range(totalItems):
    totalLength = len(items[i]) + len(itemPrices[i]) + 1
    print(items[i] + '-' * (30 - totalLength) + "$" + itemPrices[i])


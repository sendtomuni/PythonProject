import uuid

# Hardcoded item list; you may change values
items = [['laptop', 1200],
         ['mouse', 20],
         ['keyboard', 30],
         ['tablet', 200]]

item_data = {}

for item in items:
    item_data[uuid.uuid5(uuid.NAMESPACE_OID, item[0]).hex[:6]] = item


print("Item Data:")
for k, v in item_data.items():
    print(f"{k}: {v}")


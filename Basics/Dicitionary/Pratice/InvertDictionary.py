original = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3, 'f': 2}

inverted = {}

for key, value in original.items():
    if value in inverted:
        inverted[value].add(key)
    else:
        inverted[value] = {key}

# Print the inverted dictionary
print("Inverted Dict:", inverted)

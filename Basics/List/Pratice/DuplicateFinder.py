# Given list with duplicate values, can modify the list
L1 = [3, 5, 7, 9, 3, 6, 5, 2, 3, 7, 10]

# Initialize an empty list for unique elements
res = []

for item in L1:
    if item not in res:
        res.append(item)


# Write the logic below for  loop and if condtion to process the list and collect unique elements








# Print the resulting list without duplicates

print("Deduplicated List : ", res)

# Given list with duplicate values
length = int(input("enter the length of array"))
L1 = []
for i in range(0, length, 1):
    item = int(input('Enter ' + str(i) + ' item: '))
    L1.append(item)

# Initialize an empty list to store unique elements
res = []

# Iterate through each element in the given list
for element in L1:
    # Check if the element is not already in the result list
    if element not in res:
        res.append(element)  # Add it if it's not already present

# Print the list after removing duplicates
print('Deduplicated List:', res)
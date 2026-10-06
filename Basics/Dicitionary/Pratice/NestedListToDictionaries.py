header = ['name', 'age', 'city']
data = [
    ['James', 25, 'NY'],
    ['Kiran', 30, 'DEL'],
    ['Smith', 24, 'PAR'],
    ['Raj', 27, 'DEL']
]

result = []
length = len(header)

names = {}
ages = {}
cities = {}
for employee in data:
    if employee[0] not in names:
        names[employee[0]] = [employee]
    else:
        names[employee[0]].append(employee)
    if employee[1] not in ages:
        ages[employee[1]] = [employee]
    else:
        ages[employee[1]].append(employee)
    if employee[2] not in cities:
        cities[employee[2]] = [employee]
    else:
        cities[employee[2]].append(employee)

result.append(names)
result.append(ages)
result.append(cities)


# Print the results
print("Dictionaries:")
for i in range(length):
    # Print the header which defines the grouping
    print('\n' + header[i])
    for key, value in result[i].items():
        # Nicely align the keys on left side
        print(f"{key:<10}:{value}")

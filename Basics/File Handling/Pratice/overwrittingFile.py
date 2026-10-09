file = open('overwrite.txt', 'w')

str = 'Writing Version 0'

file.write(str)

file.close()

file = open('overwrite.txt', 'w')

str = 'Writing Version 1'

file.write(str)

file.close()

file = open('overwrite.txt', 'r')

data = file.read()

print(data) # Writing Version 1

file.close()
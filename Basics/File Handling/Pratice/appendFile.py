file = open('append.txt', 'a')

str = 'Writing Version 0'

file.write(str)

file.close()

file = open('append.txt', 'a')

str = 'Writing Version 1'

file.write(str)

file.close()

file = open('append.txt', 'r')

data = file.read()

print(data) # Writing Version 0Writing Version 1


file.close()
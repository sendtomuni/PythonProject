scan = 'These+notes#reveal9Newton seeking-out an{underlying structure to/the\pyramid}'
clean = ''

# TODO:Write the  Data Cleaning Logic using for loop below
for char in scan:
    if char.isalpha() or char.isspace():
        clean += char
    else:
        clean += ' '
print(clean)

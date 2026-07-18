import itertools as it

# Hardcoded list of elements
lst = ['A', 'B', 'C', 'D']

# TODO: Generate permutations of length 2 from lst
perms = it.permutations(lst, r=2)  # Replace None with itertools.permutations call



# TODO: Convert perms to a list
perm_list = list(perms)




#Print the header "Permutations"
print("Permutations")

# Iterate over perm_list and print each permutation tuple

for t in perm_list:
    print(t)

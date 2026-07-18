lists = [[1, 2, 3], [1, 1, 1, 1, 1], [2, 2, 3, 3]]


# TODO: Correctly use max() with key argument to find the longest list

max_list = max(lists, key=len)

max_list_2 = max(lists, key=lambda l: len(l))




print('Longest List:', max_list_2)

"""
claude:
Don't create lab for this
"""

import array

def missing_item(given_list):
    start = given_list[0]
    end = given_list[ len(given_list) - 1]

    actual_list = list(range(start, end + 1))
    return sum(actual_list)-sum(given_list)

arr = array.array('i', [1,2,3,5,6,7,8,9])
print(missing_item(arr))


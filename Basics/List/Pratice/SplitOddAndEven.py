# Given list of numbers, list can be tested for different numbers

nums = [4, 8, 3, 5, 10, 7, 2, 9, 13, 6]

# TODO: Create a list of all odd numbers from nums using list comptrehension.

odd = [x for x in nums if x % 2 != 0]

# TODO: Create a list of all even numbers from nums from nums using list comptrehension.

even = [x for x in nums if x % 2 == 0]


# Print the odd and even lists
print('Odd:', odd)
print('Even:', even)

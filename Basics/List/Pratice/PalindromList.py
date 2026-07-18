# Given list
lst = [5, 4, 3, 3, 4, 5]

# TODO: Create a reversed copy of lst using slicing

rev = lst[::-1]
print(lst)

if lst == rev:
    print("Yes, Palindrome")
else:
    print("Not a Palindrome")
# TODO: Compare lst and rev using if..else clause, print "Yes, Palindrome" if equal, else "Not a Palindrome"

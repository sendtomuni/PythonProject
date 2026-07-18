S1 = 'Python'

# TODO: remove spaces
S2 = S1.strip()

# TODO: reverse string
rev = S1[::-1]

if S2.casefold() == rev.casefold():
    print(S1)
else:
    # TODO: concatenate lowercase strings
    palindrome = S2.lower() + rev.lower()
    print(palindrome)

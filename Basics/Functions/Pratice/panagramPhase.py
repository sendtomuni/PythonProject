import re

def fun_anagram(pharse):
    # Remove spaces and convert to lowercase
    unique_chars = set()

    for char in pharse:
        if char.isalpha():
            unique_chars.add(char.lower())

    # Check if the number of unique characters is 26 (for English alphabet)
    if len(unique_chars) == 26:
        return True
    else:
        return False

print(fun_anagram("P1ack my box witph five dozen liquor jugs@1"))
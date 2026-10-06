import re

str1 = ('Time is the most valuable thing we have,'
        ' and once lost, it never returns.')
str2 = ("We never get time back once it's "
    "gone—it's truly the most valuable resource.")

# TODO: Extract words from both strings using regular expressions
# TODO: Create sets of words from both lists to get unique words
# TODO: Calculate intersection and union of the two sets
# TODO: Compute ratio as len(common) / len(unique)

word_set_list_1 = re.findall(r'\w+', str1.lower())
word_set_list_2 = re.findall(r'\w+', str2.lower())

word_set_list_1 = set(word_set_list_1)
word_set_list_2 = set(word_set_list_2)

common = word_set_list_1.intersection(word_set_list_2)
unique = word_set_list_1.union(word_set_list_2)

# TODO: Assign result to variable 'ratio'
ratio = len(common) / len(unique)


print(f"Jaccard Similarity:{ratio:.2f}")  # Display the similarity

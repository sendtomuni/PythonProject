word_set = {'plea', 'medical', 'listen', 'leap', 'decimal', 'silent', 'pale', 'enlist'}
result = set()
# TODO: Fill in the logic to find all scrambled/anagram pairs and add them to 'result' as sorted tuples

for word1 in word_set:
    for word2 in word_set:
        if word1 != word2 and sorted(word1) == sorted(word2): # Add as a sorted tuple to avoid duplicates
            pair = tuple(sorted((word1, word2)))
            result.add(pair)

for pair in result:
    print(pair)# Prints only unique pairs, thanks to the set


print("second approach")
result_set = set()
word_set_list = [word for word in word_set]# Convert set to list for indexing
for word3 in word_set_list:
    scrambled_list = [word3]
    for word4 in word_set_list:
        if word3 != word4 and set(word3).difference(set(word4)) == set():
            scrambled_list.append(word4)
            word_set_list.remove(word4)
    scrambled_tuple = tuple(sorted(scrambled_list))
    result_set.add(scrambled_tuple)
    scrambled_list.clear()

for pair in result_set:
    print(pair)  # Prints only unique pairs, thanks to the set
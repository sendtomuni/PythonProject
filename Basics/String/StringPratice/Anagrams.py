S1 = 'snooze alarms'
S2 = "alas, no more Zh's"

S1 = S1.lower()
S2 = S2.lower()

# TODO: Write a for loop to check each letter and compare counts. If any mismatch, print 'not anagrams' and break.
if len(S1) != len(S2):
    print("Not Anagrams")
else:
    for char in S1:
        if char.isalpha():
            if S1.count(char) != S2.count(char):
                print("Not Anagrams")
                break
    else:
        print('Anagrams')

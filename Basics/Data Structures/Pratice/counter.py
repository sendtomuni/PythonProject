import re
from collections import Counter
"""
Text:
''' Python is an easy programmers' language.
Python syntax is like the english language.
Python language is easy to learn and adapt to compared with Java and C.
In Python language, te same task can be performed using fewer lines of code.
its eay learning and easy to code'''
"""
from collections import Counter

text = ''' Python is an easy programmers' language.
Python syntax is like the english language.
Python language is easy to learn and adapt to compared with Java and C.
In Python language, te same task can be performed using fewer lines of code.
its eay learning and easy to code'''

words = re.findall('\\w+', text)

wordsCounter = Counter(words)

print(wordsCounter.most_common(3))
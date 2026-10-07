"""
caller classes are simillar to closure methods
"""

class Day:
    def __init__(self):
        self.days={0:'Sunday', 1:'Monday',
                   2:'tuesday', 3:'WednesDay',
                   4: 'Thursday', 5: 'FriDay',
                   6:'Saturday'}

    def __call__(self, dayNo):
        return self.days[dayNo][0:3].capitalize()

d = Day()
print(d(2))
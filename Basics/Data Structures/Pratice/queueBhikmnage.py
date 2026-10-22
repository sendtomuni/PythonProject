"""
claude:
Don't create lab for this
"""

from collections import deque

students = deque([1,2,3,4,5,6,7,8,9,10])

def serve(event):
    print(event, students)
    students.rotate(-1)

serve("breakfast")
serve("lunch")
serve("dinner")
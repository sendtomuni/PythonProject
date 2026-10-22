"""
claude:
Don't create lab for this
"""

import heapq

items = [11,22,2,12,25,16,17,28,10]

def sort_with_heap(items):
    sorted_items = []
    heapq.heapify(items)
    for i in range(len(items)):
        item = heapq.heappop(items)
        sorted_items.append(item)
    return sorted_items

print(sort_with_heap(items))
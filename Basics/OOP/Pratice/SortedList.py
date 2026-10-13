import bisect as bi
class SortedList:
    def __init__(self):
        self.values = []

    def func_add(self, value):
        bi.insort(self.values, value)

    def fun_remove(self, value):
        self.values.remove(value)

    def fun_search(self, value):
        return  self.values.index(value)

    def fun_insrt_pos(self, value):
        return bi.bisect_left(self.values, value)

    def display(self):
        print(self.values)
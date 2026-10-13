import heapq
class PriorityScheduler:
    class Task:
        def __init__(self, name, priority):
            self.name = name
            self.prioirty = priority

        def __repr__(self) -> str: return f'{self.name}'

    def __init__(self):
        self.task_list = []

    def func_add_task(self, name, priority):
        task = self.Task(name, priority)
        heapq.heappush(self.task_list, (priority, task))

    def next_task(self):
        if self.task_list:
            return heapq.heappop(self.task_list)
        else:
            return None

    def peek_task(self):
        if self.task_list:
            return heapq.nsmallest(1, self.task_list)
        else:
            return None

scheduler = PriorityScheduler()
scheduler.func_add_task("priority 2", 2)
scheduler.func_add_task("priority 1", 1)
print(scheduler.peek_task()) # [(1, priority 1)]
print(scheduler.next_task()) # (1, priority 1)
print(scheduler.peek_task()) # [(2, priority 2)]
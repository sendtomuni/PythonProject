import time, math

class StopWatch:
    def __init__(self):
        self.startTime = None
        self.endTime = None
        self.elapsedTime = None

    def start_timer(self):
        self.startTime = time.time()
        return self.startTime

    def stop_timer(self):
        self.endTime = time.time()
        return self.endTime

    def elapsed_time(self):
        return math.floor(self.endTime - self.startTime)

    def reset_timer(self):
        self.startTime = None
        self.endTime = None
        self.elapsedTime = None

stopwatch = StopWatch()
print(stopwatch.start_timer())
time.sleep(2)
print(stopwatch.stop_timer())
print(stopwatch.elapsed_time())

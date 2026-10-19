from threading import Condition, Thread
from time import sleep


class IPOCWithCondition:
    def __init__(self):
        self.data = 0
        self.cv = Condition()

    def put(self, data):
        self.cv.acquire()
        self.cv.wait(timeout=0)
        self.data = data
        print(f'produced {self.data}')
        self.cv.notify()
        self.cv.release()
        sleep(1)


    def get(self):
        self.cv.acquire()
        self.cv.wait()
        x = self.data
        print(f'Consumed {x}')
        self.cv.notify()
        self.cv.release()
        sleep(1)

cond = IPOCWithCondition()

def produce(cond):
    i = 1
    while True:
        cond.put(i)
        i += 1

def consume(cond):
    while True:
        cond.get()

t1 = Thread(target=lambda:produce(cond))
t2 = Thread(target=lambda:consume(cond))

t1.start()
t2.start()

t1.join()
t2.join()


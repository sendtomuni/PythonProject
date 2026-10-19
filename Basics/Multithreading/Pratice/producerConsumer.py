from threading import Lock, Thread
from time import sleep


class MyData:
    def __init__(self):
        self.data = 0
        self.flag = False
        self.lock = Lock()

    def put(self, d):
        if self.flag != False:
            pass
        else:
            self.lock.acquire()
            self.data = d
            self.flag = True
            print(f"Produced : {self.data}")
            self.lock.release()

    def get(self):
        if self.flag != True:
            pass
        else:
            self.lock.acquire()
            x = self.data
            self.flag = False
            print(f"Consumed : {self.data}")
            self.lock.release()
            return x
myData = MyData()

def produce(data):
    i = 1
    while True:
        data.put(i)
        i += 1


def consume(data):
    while True:
        data.get()

t1 = Thread(target=lambda:produce(myData))
t2 = Thread(target=lambda:consume(myData))

t1.start()
t2.start()

t1.join()
t2.join()
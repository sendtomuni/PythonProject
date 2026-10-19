from threading import *

class Multithread(Thread):
    def run(self) -> None:
        for i in range(65,91):
            print(chr(i))

mutithread = Multithread()
mutithread.start()

for i in range(65,91):
    print(i)
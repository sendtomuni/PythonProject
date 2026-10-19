from threading import Thread, Lock


def display(str1):
    lock.acquire()
    for x in str1:
        print(x)
    lock.release()

lock = Lock()

t1 = Thread(target=display, args=('HELLO WORLD',))
t2 = Thread(target=display, args=('1234567890',))

t1.start()
t2.start()

"""
Output will be random without synchronization, hence lock is there. Its called Mutex (Mutual Exchange)
"""
from threading import Lock, RLock, Condition #可重入的锁

#在同一个线程里面，可以连续调用多次acquire， 一定要注意acquire的次数要和release的次数相等
total = 0
# lock = Lock()#获取锁和释放锁需要时间，会影响性能
lock = RLock()#用RLock可以多次调用acquire，但注意acquire和release次数
def add():
    #1. dosomething1
    #2. io操作
    # 1. dosomething3
    global lock
    global total
    for i in range(1000000):
        #注意acquire和release的次数相等
        lock.acquire()
        lock.acquire()
        total += 1
        lock.release()
        lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()


#
thread1.join()
thread2.join()
print(total)

#1. 用锁会影响性能
#2. 锁会引起死锁
#死锁的情况 A（a，b）
"""
A(a、b)
acquire (a)
acquire (b)

B(a、b)
acquire (a)
acquire (b)
"""



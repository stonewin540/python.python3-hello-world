#!/usr/bin/env python
# coding=utf-8

import time
import threading
import multiprocessing


print('\n---- General ----')


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s ... %s' % (threading.current_thread().name, n))
        time.sleep(0.1)
    print('thread %s end' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


print('\n---- Incorrect ----')
balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    # balance = balance + n
    # balance = balance - n
    balance += n
    balance -= n


def run_thread(n):
    print('Thread %s will begin change with step %d' % (threading.current_thread().name, n))
    for i in range(1000000):
        change_it(n)

    global balance
    print('Thread %s did end change with balance %d' % (threading.current_thread().name, balance))


def run_thread_with_lock(n):
    print('Thread %s will begin change with step %d' % (threading.current_thread().name, n))

    global lock
    lock.acquire()
    print('Thread %s acquired' % threading.current_thread().name)
    try:
        for i in range(1000000):
            change_it(n)

        global balance
        print('Thread %s did end change with balance %d' % (threading.current_thread().name, balance))
    finally:
        lock.release()
        print('Thread %s released' % threading.current_thread().name)

balance = 0
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('At the end balance is:', balance)

print('\n---- Threading Lock ----')
balance = 0
t1 = threading.Thread(target=run_thread_with_lock, args=(5,))
t2 = threading.Thread(target=run_thread_with_lock, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('At the end balance is:', balance)


print('\n---- Infinite Loop ----')


def infinite_loop():
    print('%s:%s will start the loop' % (multiprocessing.current_process().pid, threading.current_thread().name))
    x = 0
    while True:
        x ^= 1

# Thread
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=infinite_loop)
#     t.start()

# Process
for i in range(multiprocessing.cpu_count()):
    p = multiprocessing.Process(target=infinite_loop)
    p.start()

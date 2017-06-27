#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Process
from multiprocessing import Queue
# from multiprocessing import Pool
import os
import time
import random
# import multiprocessing

# import subprocess

# print('\n---- Only work on Unix like OS ----')
# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# if 0 == pid:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s)' % (os.getpid(), pid))


# print('\n---- Multi OS process test')
#
#
# def run_process(name):
#     print('Run child process %s (%s)' % (name, os.getpid()))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     # p = Process(target=run_process, args=('test',))
#     p = Process(target=run_process, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


# print('\n---- Pool test ----')
#
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds' % (name, (end - start)))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     print('Waiting for all subprocesses done...')
#
#     cpu_count = multiprocessing.cpu_count()
#     print('Count of your CPU is:', cpu_count)
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     p.close()
#     p.join()
#
#     print('All subprocesses done.')


# print('\n---- Subprocess call ----')
# command = 'nslookup'
# argument1 = 'www.python.org'
# print('$ %s %s' % (command, argument1))
# r = subprocess.call([command, argument1])
# print('Exit code:', r)
#
# print('\n---- Subprocess interactive call ----')
# print('$', command)
# p = subprocess.Popen([command], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# (output, error) = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)
#
# command = 'python3'
# print('$', command)
# p = subprocess.Popen([command], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# (output, error) = p.communicate(b'help(\'copyright\')\nexit()\n')
# if error:
#     print('perform', command, 'error:', error)
# else:
#     print(output.decode('utf-8'))
# print('Exit code:', p.returncode)
#
# print('\n\n---- Multi arguments ----')
# command = 'ls'
# argument1 = '-l'
# argument2 = '-a'
# print('$ %s %s' % (command, argument1))
# r = subprocess.call([command, argument1, argument2])
# print('Exit code:', r)

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

#!/usr/bin/env python
# coding=utf-8

"""
I am worker
"""

import time
from ProcessThread.Distributing.task_queue_manager import *

print('Connect to server %s...' % Constant.SERVER_ADDRESS.value)

m = QueueManager.default_manager()
try:
    m.connect()
except ConnectionError as an_error:
    print('Oh god', an_error)
else:
    task = m.get_task_queue()
    result = m.get_result_queue()

    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d' % (n, n))
            r = '%d * %d = %d' % (n, n, n * n)
            time.sleep(1)
            result.put(r)
        except Queue.Empty:
            print('task queue is empty.')

    print('worker exit.')

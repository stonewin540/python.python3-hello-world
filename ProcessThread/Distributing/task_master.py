#!/usr/bin/env python
# coding=utf-8

"""
I am master
"""

import random
from ProcessThread.Distributing.task_queue_manager import *

manager = QueueManager.default_manager()
manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)

print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)

manager.shutdown()
print('master exit.')

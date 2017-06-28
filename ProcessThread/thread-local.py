#!/usr/bin/env python
# coding=utf-8

import threading

local_school = threading.local()
attribute_name = 'student'


def process_student():
    # std = local_school.student
    std = local_school.__getattribute__(attribute_name)
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # local_school.student = name
    local_school.__setattr__(attribute_name, name)
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

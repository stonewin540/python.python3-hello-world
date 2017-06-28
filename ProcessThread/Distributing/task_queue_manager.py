#!/usr/bin/evn python
# coding=utf-8

from queue import Queue
from multiprocessing.managers import BaseManager
from enum import Enum


class Constant(Enum):
    """What's the f**k? 枚举还能这么玩？"""

    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 5000
    SERVER_AUTH_KEY = b'abc'

    SERVER_ADDRESS_TUPLE = (SERVER_ADDRESS, SERVER_PORT)


class QueueManager(BaseManager):
    _task_queue = None
    _result_queue = None

    @staticmethod
    def get_task_queue():
        if QueueManager._task_queue is None:
            QueueManager._task_queue = Queue()
        return QueueManager._task_queue

    @staticmethod
    def get_result_queue():
        if QueueManager._result_queue is None:
            QueueManager._result_queue = Queue()
        return QueueManager._result_queue

    @classmethod
    def register_queue(cls):
        QueueManager.register('get_task_queue', callable=QueueManager.get_task_queue)
        QueueManager.register('get_result_queue', callable=QueueManager.get_result_queue)

    @classmethod
    def default_manager(cls):
        QueueManager.register_queue()
        return QueueManager(Constant.SERVER_ADDRESS_TUPLE.value, Constant.SERVER_AUTH_KEY.value)

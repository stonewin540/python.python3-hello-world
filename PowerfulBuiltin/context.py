#!/usr/bin/env python
# coding=utf-8

import inspect
from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen

# ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)
# @http://blog.csdn.net/hshl1214/article/details/52130048
import ssl

file_name = 'base64.py'


f = None

print('\n---- Try ----')
try:
    f = open(file_name, 'r')
    print(f.read(100))
except IOError as an_error:
    print(an_error)
finally:
    f.close()


print('\n---- With ----')
with open(file_name, 'r') as file:
    print(file.read(100))


print('\n---- Enter & Exit')


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(inspect.currentframe().f_code.co_name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(exc_type)
        else:
            print(inspect.currentframe().f_code.co_name)

    def query(self):
        print('Query info about \'%s\'' % self.name)


with Query('stone') as q:
    q.query()


print('\n---- context manger ----')


class QueryContext(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('%s queries info about %s' % (str(self.__class__.__name__), self.name))


@contextmanager
def create_query_context_with_name(name):
    print('Begin in %s' % str(inspect.currentframe().f_code.co_name))
    q = QueryContext(name)
    yield q
    print('End in %s' % str(inspect.currentframe().f_code.co_name))


with create_query_context_with_name('stone') as q:
    q.query()


print('\n---- context manager extension ----')


@contextmanager
def tag(name):
    print('<begin %s>' % name)
    yield
    print('</end %s>' % name)

with tag('html') as tag:
    print('Hello, ')
    print('World!')


print('\n---- closing ----')

ssl._create_default_https_context = ssl._create_unverified_context
with closing(urlopen('https://www.python.org')) as page:
    # for line in page:
    #     print(line)
    print(page)

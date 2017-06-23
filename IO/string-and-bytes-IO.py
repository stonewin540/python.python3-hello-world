#!/usr/bin/env python
# coding=utf-8

from io import StringIO
from io import BytesIO
import os

print('\n---- Write directly ----')
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())


print('\n---- Write by init ----')
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


print('\n---- BytesIO ----')
print('---- Encode ----')
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
f.seek(0, os.SEEK_SET)
f.write('中文'.encode('BIG5'))
print(f.getvalue())

print('\n---- Decode ----')
f = BytesIO(b'\xa4\xa4\xa4\xe5\x96\x87')
print(f.read())

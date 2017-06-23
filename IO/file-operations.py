#!/usr/bin/env python
# coding=utf-8

import os
import shutil
import time

print(os.name)
print(os.uname())
print(os.environ)

print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))
print(os.environ.get('PYTHONPATH'))

print('\n---- Path ----')
print(os.path.abspath('.'))
print(os.path.join('~', 'test-dir'))
path = os.path.join(os.path.abspath('.'), 'test-dir')
os.mkdir(path)
os.rmdir(path)

print(path)
print(os.path.split(path))

path = os.path.join(os.path.abspath('.'), 'python.png')
print(path)
print(os.path.splitext(path))


print('\n---- File ----')
file_name = 'test.txt'
if not os.path.exists(os.path.join(os.path.abspath('.'), file_name)):
    with open(file_name, 'x') as file:
        pass

file_rename = 'test.py'
os.rename(file_name, file_rename)
os.remove(file_rename)


print('\n---- Copy File ----')
path = os.path.abspath('.')
parent_path = os.path.abspath('..')
file_name = 'README.md'
if os.path.exists(os.path.join(parent_path, file_name)):
    shutil.copyfile(os.path.join(parent_path, file_name), os.path.join(path, file_name))
    input('Can you see a duplicated %s?\nAny key to remove it.' % file_name)
    os.remove(os.path.join(path, file_name))


print('\n---- Use copyfile() for directory ----')
directory_name = 'UnitTest'
if os.path.exists(os.path.join(parent_path, directory_name)):
    try:
        shutil.copyfile(os.path.join(parent_path, directory_name), os.path.join(path, directory_name))
        input('Can you see a duplicated directory named %s?\nAny key to remove' % directory_name)
        os.remove(os.path.join(path, directory_name))
    except IsADirectoryError as an_error:
        print(an_error)
        print('copyfile() can not respond to directory')


print('\n---- Use copy() for directory')
src = os.path.join(parent_path, directory_name)
dst = os.path.join(path, directory_name)
if os.path.exists(src):
    try:
        shutil.copy(src, dst)
        input('Can you see a duplicated directory named %s?\nAny key to remove' % directory_name)
        os.remove(dst)
    except IsADirectoryError as an_error:
        print(an_error)
        print('copy() can not respond to directory')


print('\n---- Use copytree() for directory')
src = os.path.join(parent_path, directory_name)
dst = os.path.join(path, directory_name)
if os.path.exists(dst):
    shutil.rmtree(dst)
if os.path.exists(src):
    try:
        shutil.copytree(src, dst)
        input('Can you see a duplicated directory named %s?\nAny key to remove' % directory_name)
        os.removedirs(dst)
    except IsADirectoryError as an_error:
        print(an_error)
        print('copytree() can not respond to directory')
    except OSError as an_error:
        print(an_error)
        print('os.remove() or os.removedirs() are not the key func, let us try the shutil.rmtree()')
        shutil.rmtree(dst)


print('\n---- List ----')
directory_name = os.path.expanduser('~')
print(os.listdir(directory_name))
print('---- After filtration ----')
dirs = [x for x in os.listdir(directory_name) if os.path.isdir(os.path.join(directory_name, x))]
print(dirs)
dirs = [x for x in os.listdir(directory_name) if '.' in os.path.join(directory_name, x)]
print(dirs)

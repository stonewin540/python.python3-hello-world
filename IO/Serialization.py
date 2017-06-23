#!/usr/bin/env python
# coding=utf-8

import pickle
import json

d = dict(name='Bob', age=20, score=28)
print('d:', d)
bytes_string = pickle.dumps(d)
print('After pickle:', bytes_string)

print('\n---- Pickling ----')
file_name = 'dump.txt'
f = open(file_name, 'wb')
pickle.dump(d, f)
print('Dumped to file')
f.close()

print('\n---- Read from file ----')
f = open(file_name, 'rb')
d = pickle.load(f)
f.close()
print(d)


print('\n---- The important thing -- JSON ----')
d = dict(name='JSON', age=20, score=88)
json_string = json.dumps(d)
print(json_string)

print('\n---- Write ----')
file_name = 'dump_json.txt'
f = open(file_name, 'w')
json.dump(d, f)
f.close()
print('write success')

print('\n---- Read ----')
f = open(file_name, 'r')
d = json.load(f)
f.close()
print(type(d))
print(d)


print('\n---- Advanced JSON ----')


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('stone', 18, 99)
try:
    print(json.dumps(s))
except TypeError as an_error:
    print(an_error)


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('stone', 18, 99)
try:
    print(json.dumps(s, default=student2dict))
except TypeError as an_error:
    print(an_error)


def dict2student(dic):
    return Student(dic['name'], dic['age'], dic['score'])

json_string = r'{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_string, object_hook=dict2student))

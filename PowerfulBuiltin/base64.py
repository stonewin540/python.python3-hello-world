#!/usr/bin/env python
# coding=utf-8

import base64

bytes_string = b'binary\x00string'
print('Bytes string is:', bytes_string)
result = base64.b64encode(bytes_string)
print('encode PowerfulBuiltin is: ', result)
result = base64.b64decode(result)
print('decode PowerfulBuiltin is:', result)


bytes_string = b'i\xb7\x1d\xfb\xef\xff'
print('\n\nBytes string is:', bytes_string)
result = base64.b64encode(bytes_string)
print('encode PowerfulBuiltin is:', result)
result = base64.urlsafe_b64encode(bytes_string)
print('url safe encode PowerfulBuiltin is:', result)
result = base64.urlsafe_b64decode(result)
print('url safe decode PowerfulBuiltin is:', result)

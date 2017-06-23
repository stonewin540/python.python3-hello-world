#!/usr/bin/env python
# coding=utf-8

import os
import inspect


def remove_if_possible(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


def prompt_to_remove(file_name):
    prompt = 'We will remove \'' + file_name + '\' file, y/n?'
    confirm = ('y', 'yes')
    cancel = ('n', 'no')
    choice = confirm + cancel

    user_input = ''
    while not (user_input in choice):
        user_input = input(prompt).lower()

        if user_input in confirm:
            remove_if_possible(file_name)
            break
        elif user_input in cancel:
            break


def read_file_with_try(file_name):
    print('\n---- from', inspect.currentframe().f_code.co_name)
    f = None
    try:
        f = open(file_name, 'r')
        print(f.read())
    except IOError as an_error:
        print(an_error)
    finally:
        if f:
            f.close()


def read_file_with_with(file_name):
    print('\n---- from', inspect.currentframe().f_code.co_name)
    try:
        with open(file_name, 'r') as f:
            print(f.read())
    except IOError as an_error:
        print(an_error)


def create(file_name):
    try:
        f = open(file_name, 'x')
        f.write('Hello, World!')
        f.close()
    except IOError as an_error:
        print(an_error)
    finally:
        if f:
            f.close()


def update_to_multiple(file_name):
    print('\nIn', inspect.currentframe().f_code.co_name)
    try:
        with open(file_name, 'w') as f:
            f.seek(0, os.SEEK_SET)

            numbers = ('One', 'Two', 'Three', 'Four', 'Five', 'Enh, this is multiple line file')
            string = ''
            for number in numbers:
                string = string + number
                if number != numbers[-1]:
                    string = string + '\n'

            f.writelines(string)
    except IOError as an_error:
        print(an_error)


def read_file_line(file_name):
    print('\nIn', inspect.currentframe().f_code.co_name)
    try:
        with open(file_name) as file:
            print('---- read line ----')
            count = 3
            while count > 0:
                count -= 1

                print('current position', file.tell())
                print(file.readline())

            print()
            print('---- read lines default ----')
            print('current position', file.tell())
            print(file.readlines())

            hint = 10
            print('\ncurrent position', file.tell())
            pos = os.SEEK_SET
            print('move to', pos, file.seek(0, os.SEEK_SET))
            print('read lines', hint)
            print(file.readlines(hint))
    except IOError as an_error:
        print(an_error)


def read_png_if_possible():
    print('\nIn', inspect.currentframe().f_code.co_name)

    file_name = 'python.png'
    try:
        with open(file_name, 'r') as file:
            print('---- open as \'r\' mode ----')
            print(file.read())
    except (IOError, UnicodeDecodeError) as an_error:
        print(an_error)

    print()
    try:
        with open(file_name, 'rb') as file:
            print('---- open as \'rb\' mode ----')
            print(file.read())
    except (IOError, UnicodeDecodeError) as an_error:
        print(an_error)


# main business logic
FILE_NAME = 'test.txt'

# try style
remove_if_possible(FILE_NAME)
read_file_with_try(FILE_NAME)
create(FILE_NAME)
read_file_with_try(FILE_NAME)

# with style
remove_if_possible(FILE_NAME)
read_file_with_with(FILE_NAME)
create(FILE_NAME)
read_file_with_with(FILE_NAME)

# multiple line
update_to_multiple(FILE_NAME)
read_file_with_with(FILE_NAME)
read_file_line(FILE_NAME)


# PNG file
read_png_if_possible()

# finish work
prompt_to_remove(FILE_NAME)

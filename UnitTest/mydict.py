#!/usr/bin/env python3
# coding=utf-8


class Dict(dict):
    def __init__(self, **kwargs):
        # super(Dic, self).__init__(**kwargs)
        super().__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

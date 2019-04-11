from __future__ import (absolute_import, division, print_function, unicode_literals)

from .klass_serie import Serie


class DF(object):
    def __init__(self, arg={}):
        assert isinstance(arg, list), "The argument should be a list"
        self.data = arg

    def add(self, name, data):
        self.data[name] = Serie(data)

    def remove(self, name):
        if name in self.data:
            del self.data[name]

    def __getitem__(self, item):
        return self.data[item]

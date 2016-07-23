#!/usr/bin/env python2

class Stack(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.temp = []

    def push(self, value):
        list.append(self, value)

    def pop(self):
        if len(self) == 0:
            return 0
        return list.pop(self)

    def peek(self):
        if len(self) == 0:
            return 0
        return self[-1]

    def get(self):
        return self

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

    def get(self):
        return self

    def clear(self):
        self = Stack([])
        self.temp = None

    def peek(self):
        if len(self) == 0:
            return 0
        return self[-1]

    def weave(self, other):
        if len(self) == len(other):
            weaved = sum(zip(self, other), [])
        else:
            stacks = sorted([self, other])
            extra = reduce(lambda a,b:a-b, map(len, stacks))
            weaved = sum(zip(*stacks), [])
            weaved += stacks[1][-abs(extra):]
        return Stack(weaved)

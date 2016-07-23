import re
from getch import getch # From https://gist.github.com/chao787/2652257

BAA = re.compile(r"ba{2,}")
BLEET = re.compile(r"ble{2,}t")

def gaot(s):
    stack = []
    t = s.split()
    i = 0
    d = 1
    while i < len(t):
        c = t[i]
        if BAA.search(c):
            stack.append(len(c) - 2)
        elif BLEET.search(c):
            n = len(c) - 3
            if n == 2:
                stack.append(stack.pop() + stack.pop())
            elif n == 3:
                stack.append(stack.pop(-2) - stack.pop())
            elif n == 4:
                i += d
            elif n == 5:
                break
            elif n == 6:
                d = -d
            elif n == 7:
                if stack.pop():
                    i += d
            elif n == 8:
                if not stack.pop():
                    i += d
            elif n == 9:
                print(stack.pop())
            elif n == 10:
                print(chr(stack.pop()), end="")
            elif n == 11:
                stack.append(int(input()))
            elif n == 12:
                stack.append(ord(getch()))
            elif n == 13:
                stack.append(stack[-1])
            elif n == 14:
                stack.append(stack.pop(-2))
            elif n == 15:
                stack.reverse()
        i += d

import sys
with open(sys.argv[1]) as f:
    g = f.read()
gaot(g)

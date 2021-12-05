#!/usr/bin/env python

import re
import sys
from getch import getch # From https://gist.github.com/chao787/2652257
from stack import Stack

try:
    raw_input
except NameError:
    raw_input = input


class Gaot(object):
	def __init__(self):
		self.stack = Stack([])
		self.instructions = None
		self.ipointer = 0
		self.move = 1
		self.BAA = re.compile(r"ba{2,}")
		self.BLEET = re.compile(r"ble{2,}t")

		self.commands = [self._add,        #2
					   self._subtract,     #3
					   self._continue,     #4
					   self._exit,         #5
					   self._reverse,      #6
					   self._skiptrue,     #7
					   self._skipfalse,    #8
					   self._printnum,     #9
					   self._printchar,    #10
					   self._getnum,       #11
					   self._getchar,      #12
					   self._dupe,         #13
					   self._swap,         #14
					   self._reverse_stack,#15
					   self._rotate_stack] #16
		self.ccount = 0

	def run(self, program):
		self.instructions = program.split()
		while self.ipointer < len(self.instructions) and self.ipointer >= 0:
			c = self.instructions[self.ipointer]

			if self.BAA.search(c): # is a "baa" command
				self.stack.append(len(c) - 2)

			elif self.BLEET.search(c): # is a "bleet" command
				n = len(c) - 3
				self.commands[n-2]()
			self.ipointer += self.move

	def get_code(self):
		if "--file" in sys.argv:
			code = open(sys.argv[sys.argv.index("--file") + 1]).read()

			input_index = sys.argv.index("--file")

			sys.argv.pop(sys.argv.index("--file") + 1)
			sys.argv.pop(sys.argv.index("--file"))

		elif len(sys.argv) >= 2:
			code = sys.argv[1]
			input_index = 2
		else:
			code = raw_input("Code: ")

		try:
			self.input = sys.argv[input_index:]
		except:
			self.input = []
		return code


	# --------------------------------------

	def _add(self):
		self.stack.push(self.stack.pop() + self.stack.pop())

	def _subtract(self):
		self.stack.push(self.stack.pop() - self.stack.pop())

	def _continue(self):
		self.ipointer += self.move

	def _exit(self):
		exit()

	def _reverse(self):
		self.move *= -1

	def __skip(self, state):
		self.ipointer += self.move*(self.stack.pop() == state)

	def _skiptrue(self):
		self.__skip(True)

	def _skipfalse(self):
		self.__skip(False)

	def _printnum(self):
		sys.stdout.write(unicode(self.stack.pop()))
		sys.stdout.flush()

	def _printchar(self):
		sys.stdout.write(unicode(chr(self.stack.pop())))
		sys.stdout.flush()

	def _getnum(self):
		self.stack.push(float(raw_input()))

	def _getchar(self):
		# check if stdin is connected to a terminal
		if sys.stdin.isatty():
			_ = ord(getch())
			self.stack.append(_*(_!=4))
		else:
			# getch() doesn't work with non-terminals
			ch = sys.stdin.read(1)
			if ch == '':
				self.stack.append(0)
			else:
				self.stack.append(ord(ch))

	def _dupe(self):
		self.stack.push(self.stack.peek())

	def _swap(self):
		x,y = self.stack.pop(), self.stack.pop()

		self.stack.push(x)
		self.stack.push(y)

	def _reverse_stack(self):
		self.stack = Stack(self.stack.get()[::-1])

	def _rotate_stack(self):
		x = self.stack[0]
		self.stack = Stack(self.stack[1:])
		self.stack.push(x)

def main():
    gaot = Gaot()
    gaot.run(gaot.get_code())

if __name__ == "__main__":
    main()

import sys
from calc26 import *

def calc(a,c,b):

	a10 = int(convert_26_to_10(a))
	b10 = int(convert_26_to_10(b))

	print a+": "+str(a10)
	print b+": "+str(b10)

	if c == '+':
		return convert_10_to_26(a10+b10)
	elif c == '-':
		return convert_10_to_26(a10-b10)
	elif c == '*':
		return convert_10_to_26(a10*b10)

if __name__ == '__main__':
	s = (sys.argv[1]).split()
	a = s[0]
	c = s[1]
	b = s[2]

	ans = calc(a,c,b)
	print "Answer: "+ans
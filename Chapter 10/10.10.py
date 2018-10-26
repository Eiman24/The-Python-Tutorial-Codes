'''
Performance Measurement
'''
from timeit import Timer

timea = Timer(
	't = a; a = b; b = t',
	'a = 1; b = 2'
	).timeit()

timeb = Timer(
	'a,b = b,a',
	'a = 1; b = 2'
	).timeit()

print(timea, timeb)
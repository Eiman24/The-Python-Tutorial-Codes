# This example also introduces the in keyword. 
# This tests whether or not a sequence contains a certain value.

def ask_ok(prompt, retries = 4, reminder = 'plase try again!'):
	while True:
		ok = input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no','nop','nope'):
			return False
		retries -= 1
		if retries < 0:
			raise ValueError('invalid user response')
		print(reminder)


answer = ask_ok('Do you really want to quit?')
print(answer)

#----------------------------------------------------------------#

# The default values are evaluated at the point of 
# function definition in the defining scope.

i = 5

def f(arg = i):
	print(arg)

i = 0
f()

#----------------------------------------------------------------#

# When the default is a mutable object such as a list,dic,class,
# evaluate won't appear only onece.

def f(a, L = []):
	L.append(a)
	return L

print(f(1))
print(f(2))
print(f(3))

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))

#----------------------------------------------------------------#

# Functions can also be called using keyword arguments of the form kwarg=value.

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(voltage=1000000, action='VOOOOOM')
parrot(action='VOOOOOM', voltage=1000000)
parrot('a thousand', state='pushing up the daisies')
# Defining Functions

def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	# print() default print '\n'
	print()

fib(2000)
fib(10000)


# Global variables cannot be directly assigned a value within a function 
# (unless named in a global statement), although they may be referenced.

# The actual parameters (arguments) to a function call are introduced 
# in the local symbol table of the called function when it is called.

# When a function calls another function, a new local symbol table is created for that call.


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result


print(fib2(100))
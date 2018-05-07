from fibo import fib, fib2
# or import all
# from fibo import *

# None is printed because there is a print() in other print()
a = fib(500)
print(a)

import fibo as fib

print(fib.fib2(500))

from fibo import fib as fibonacci
print(fibonacci(500))
# Class objects support two kinds of operations: attribute references and instantiation.
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return "hello world"

## MyClass.i and MyClass.f are valid attribute references
print(MyClass.i)
print(MyClass.f)
print(MyClass.f(1))
print(MyClass.__doc__)
# You can change the value of MyClass.i by assignment.
MyClass.i = 123
print(MyClass.i)


## Class instantiation uses function notation.
class Complex:
    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart

x = Complex(3.0, -4.5)
print(x.r, x.i)

# Data attributes need not be declared; like local variabless, 
# they spring into existence when they are first assigned to. 
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

y = MyClass()
print(y.f())
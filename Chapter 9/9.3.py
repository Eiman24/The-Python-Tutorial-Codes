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

#  instance variables are for data unique to each instance 
# and class variables are for attributes and methods shared by all instances of the class
class Dog:
    
    kind = 'canine'
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind, e.kind)
print(d.name, e.name)

# the mutable object list 'tricks[]' is unexpectedly shared by all dogs
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

# Correct the unexpected sharing above
class Dog2:
    
    kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog2('Fido')
e = Dog2('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)
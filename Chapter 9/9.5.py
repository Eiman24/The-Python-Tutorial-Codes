# Use isinstance() to check an instance’s type: 
# isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.
# isinstance(obj, int)
obj1 = int()
obj2 = float()
print(isinstance(obj1, int), isinstance(obj2, int))

# Use issubclass() to check class inheritance: 
# issubclass(bool, int) is True since bool is a subclass of int. However, 
# issubclass(float, int) is False since float is not a subclass of int.
print(issubclass(bool, int), issubclass(float, int))
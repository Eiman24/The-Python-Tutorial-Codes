t = 12345, 54321, 'hello!'
print(t[0])

u = t, (1, 2, 3, 4, 5)
print(u)

# tuple does not support item assignment

# tuple can contain mutable objects
v = ([1, 2, 3], [3, 2, 1])
print(v)

empty = ()
singleton = 'hello', # <- note trailing comma

print(len(empty),len(singleton))
print(singleton)

# sequence unpacking
x, y, z = t
print(x, y, z)
# It is best to think of a dictionary as an unordered set of key: value pairs, 
# with the requirement that the keys are unique (within one dictionary). 

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
print(tel)

tel['irv'] = 4127
print(tel)

telkeys = list(tel.keys())
print(telkeys)
telvalues = list(tel.values())
print(telvalues)

print('guido' in tel)
print('sape' in tel)
print('jack' not in tel)

# use dict() to build dictionaries
# values can be same
tel2 = dict([('sape', 4139), ('pikachu', 'pikapika!'),('jack', 4139)])
print(tel2)

# dict comprehensions
tel3 = {x: x**2 for x in (2, 4, 6)}
print(tel3)

# unsing keyword arguments
tel4 = dict(sape=4139, guido=4127, jack=4098)
print(tel4)
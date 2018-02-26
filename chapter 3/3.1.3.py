squares = [1,4,9,16,25]
# lists can be indexed and sliced
print(squares[-1])
print(squares[-3:])
# lists support operations like concatenation
print(squares + [36, 49, 64, 81, 100])
# are a mutable type
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)
# Assignment to slices
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)
print(len(letters))
# list nesting
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count("apple"))

print(fruits.count("tangerine"))

print(fruits.index("banana"))

# Find next banana starting a position 4
print(fruits.index("banana",4))

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

# remove and return the last item in the list if no index is specified.
print(fruits.pop())
print(fruits)
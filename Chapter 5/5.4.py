# A set is an unordered collection with no duplicate elements

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

# fast membership testing
print('orange' in basket)
print('crabgrass' in basket)

# to creat an empty set, you have to use set() instead of{}
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)	# letters in a but not in b
print(a | b)	# letters in a or b or both
print(a & b)	# letters in both a and b
print(a ^ b)	# letters in a or b but not both 对称差
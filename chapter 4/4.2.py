import time

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# With for w in words:, 
# the example would attempt to create an infinite list, 
# inserting defenestrate over and over again.
for w in words[:]:
	if len(w) > 6:
		words.insert(0,w)
print(words)


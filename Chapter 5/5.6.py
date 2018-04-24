# items()
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)

# enmuerate 枚举
for i, v in enumerate(['tic', 'tac', 'toc']):
	print(i, v)

# zip() should use dict to process a zip object to a dictionary
dic = {x:x*2 for x in range(1,4)}
print(dic)
for a, b in dic.items():
	print(a, b)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
dic2 = dict(zip(questions, answers))
print(dic2)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# reversed()
for i in reversed(range(1, 10, 2)):
	print(i)
# sorted()
basket = ['apple', 'orange','apple','pear','orange','banana']
for f in sorted(set(basket)):
	print(f)

# instead of change a list while looping over it,
# it is often simpler and safer to create a new list instead.

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
	if not math.isnan(value):
		filtered_data.append(value)
print(filtered_data)
class Mapping:
	"""docstring for Mapping"""
	def __init__(self, iterable = ''):
		self.items_list = []
		self.__update(iterable)

	def update(self, iterable):
		for item in iterable:
			self.items_list.append(item)

	__update = update    # private copy of original update() method, (变量传递)

class MappingSubclass(Mapping):
	"""docstring for MappingSubclass"""
	def update(self, keys, values):
		# provides new signature for update()
		# but does not break __init__()
		for item in zip(keys, values):
			self.items_list.append(item)
		
list1 = ['a','b' ,'c' ,'d' ,'e' ,'f' ,'g']
list2 = [1, 2 ,3 ,4 ,5 ,6 ,7]
M2 = MappingSubclass()
M2.update(list1, list2)
print(M2.items_list)
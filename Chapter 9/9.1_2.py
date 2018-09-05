def scope_test():
	def do_local():
		spam = "local spam"

	def do_nonlocal():
		nonlocal spam
		spam = "nonlocal spam"

	def do_global():
		global spam
		spam = "global spam"

	spam = "test spam"
	# 函数内的变量，不会影响外层
	do_local()
	print("After local assignment: ", spam)
	# nonlocal 将变量定义到外面一层，既line13的spam
	do_nonlocal()
	print("After nonlocal assignment:", spam)
	# 定义了全局变量spam，
	do_global()
	print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# A class is never used as a global scope.
# 类函数定义也可以通过赋值的形式完成，函数可以在类外面
def f1(self, x, y):
	return(min(x, x+y))

class C:
	f = f1

	def g(self):
		return 'hello world'

	h = g

sampleC = C()
print(sampleC.f(2, -3))
print(sampleC.h(), sampleC.g())

# 方法可以利用self调用其他方法
class Bag:
	def __init__(self):
		self.data = []

	def add(self, x):
		self.data.append(x)

	def addtwice(self, x):
		self.add(x)
		self.add(x)

TextBag = Bag()
TextBag.add(6)
print(TextBag.data)
TextBag.addtwice(5)
print(TextBag.data)
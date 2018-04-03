list1 = list(map(lambda x: x**2, range(10)))
print(list1)

list2 = [x**2 for x in range(10)]
print(list2)

list3 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(list3)

vec = [[1,2,3], [4,5,6], [7,8,9]]
list4 = [num for elem in vec for num in elem]
print(list4)
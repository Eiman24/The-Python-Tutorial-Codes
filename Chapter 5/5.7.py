# A and not B or C is equivalent to (A and (not B)) or C
# 从左侧开始判断 
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

# null is '0' in Bool
a = ''
if not a:
	print("ok")
a = ''
if  a:
	print("ok")

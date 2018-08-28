# multiple assignment
#为末尾end传递一个','，这样print函数不会在字符串末尾添加一个换行符。
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b
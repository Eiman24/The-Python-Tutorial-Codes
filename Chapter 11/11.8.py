from decimal import *

Decimalresult = round(Decimal('0.70')*Decimal('1.05'), 2)
print(Decimalresult)

Binaryresult = round(.7*1.05, 2)
print(Binaryresult)

print(Decimal('1')%Decimal('0.1'))
print(1%0.1)

getcontext().prec = 36 # 精确度
print(Decimal(1) / Decimal(7))
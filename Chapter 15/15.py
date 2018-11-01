import math

print(format(math.pi, '.12g'))  # give 12 significant digits
print(format(math.pi, '.2f'))   # give 2 digits after the point
print(repr(math.pi))

print(round(.1, 10) + round(.1, 10) + round(.1, 10) == round(.3, 10))
a = 0.1 + 0.1 + 0.1
b = 0.3
print(round(a, 1) == round(b, 1))
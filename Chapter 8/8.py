while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")


class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

raise NameError('HiThere')

raise ValueError

# The problem with this code is that it leaves the file open for an 
# indeterminate amount of time after this part of the code has finished executing. 
for line in open("myfile.txt"):
    print(line, end="")
# After the statement is executed, the file f is always closed, 
# even if a problem was encountered while processing the lines.
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
import os
print(os.getcwd()) # Current working diredtary
# print(os.chdir(r'C:\python projects\The-Python-Tutorial-Codes\Chapter 9'))
# print(os.getcwd())
print(os.system('mkdir today'))

print(dir(os))
print(help(os))

import glob
print(glob.glob('*.py'))

import sys
print(sys.argv)
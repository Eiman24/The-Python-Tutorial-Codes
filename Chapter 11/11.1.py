import reprlib

a = reprlib.repr(set('supercalifragilisticexpialidocious'))
print(a)

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width = 30)
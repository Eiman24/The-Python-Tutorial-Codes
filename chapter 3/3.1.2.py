print('spam eggs')
print('doesn\'t')
print("doesn't")
print('"Yes," he said.')
print("\"Yes,\" he said.")
print('"Isn\'t," she said.')

s = 'First line.\nSecond line.'
print(s)

# If you don’t want characters prefaced by \ to be interpreted as special characters,
# you can use raw strings by adding an r before the first quote:
print('C:\some\name')
print(r'C:\some\name')

# String literals can span multiple lines using triple-quotes:
print("""\
Usage: thingy [OPTIONS]
     -h     
     -H hostname#ddd
""")

# concatenated with +, and repeated with *:
print(3 * 'un' + 'ium')

text = ('Put several strings within parentheses '
'to have them joined together.')
print(text)

# String indexed,negative stand for counting from right:
word = 'Python'
print(word[0],word[-1])

s = 'supercalifragilisticexpialidocious'
print(len(s))
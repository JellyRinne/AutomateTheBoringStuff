print('Hello, World! I\'m a python script! Here\'s some stuff I know!') #You can't see this comment!
print()
print('5+5 is: ' + str(int(5 + 5)))
print()
print('42 % 6 is: ' + str(int(42 % 6)))
print()
print('2 ** 3 is: ' + str(int(2 ** 3)))
print()

spam = 'Hello,'
eggs = ' World!'
print(spam + eggs)

waffles = 4
waffles = waffles + 8
breakfast = spam + eggs + ' Peter is ' + str(waffles) + ' apples tall. '
print(breakfast)
print('\nNewlines can be more efficient than "print()", try "\\n"!')
breakfast = '\n' + breakfast
print(breakfast * 3)
print('\n(5-1) * ((7 + 1) / (3 - 1))' ' = ' + str(int((5-1) * ((7 + 1) / (3 - 1)))))
print('\nPython variable rules:')
print('1. It can only be one "word" with no spaces.')
print('2. It can only use letters, numbers, and underscores.') 
print('3. It can\'t begin wtih a number.')

print('\nHello, World! What\'s your name?')
myName = input()
print('\nNice to meet you, ' + myName + '!') #input() always returns a string!
print('The length of your name is: ' + str(len(myName))) #but a length of a string is an integer, so convert it back!
print('\nHow old are you?')
myAge = input()
print('\nYou will be ' + str(int(myAge) + 5) + ' in 5 years!')

#Practice Questions:
#1: 
# * - operator
# 'hello' - value
# -88.8 - value
# - - operator
# / - operator
# + - operator
# 5 - value

#2:
# spam - variable
# 'spam' - string

#3:
# String, Integer, Float

#4:
# an expression is made up of values and operators, and evaluates down to a single value

#5:
# a statement assigns a value to a variable, an expression evaluates values and operators down to a single value. a statement can contain an expression.

#6:
# 21

#7:
# spamspamspam
# spamspamspam

#8:
# a variable's name cannot be or begin with an integer

#9:
# int(), float(), str()

#10:
# the integer is not converted to a string. a + operator after a string will concatenate the string with the following value, and integers and floats cannot be concatenated.


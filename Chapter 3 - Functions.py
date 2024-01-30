import random

def hello():
    print('Howdy!')
    print('Howdy!!')
    print('Hello there.\n')

hello()
hello()
hello()

def hello2(name):
    print('Hello, ' + name)

hello2('Alice')
hello2('Bob\n')

def magic8Ball(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not good'
    elif answerNumber == 9:
        return 'Very doubtful'
    else:
        return 'Fuck off'

r = random.randint(1,9)
fortune = magic8Ball(r)
print(fortune + '\n')
#or
print(magic8Ball(random.randint(1, 9)) + '\n')

print('"print()" includes an imlicit newline at the end of what it\'s passed, so:')
print('    print(\'hello\')')
print('    print(\'world\')')
print('returns:')
print('    hello')
print('    world')
print('We can modify this using end, so:')
print('    print(\'hello\', end = \'\')')
print('    print(\'world\')')
print('returns:')
print('    helloworld')

print('\nwe can also separate arguments with sep, so:')
print('    print(\'cats\', \'dogs\', \'mice\')')
print('returns:')
print('    cats dogs mice')
print('but:')
print('    print(\'cats\', \'dogs\', \'mice\', sep = \',\')')
print('returns:')
print('    cats,dogs,mice')

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

print()

#scope demo
def spam():
    eggs = 'spam local'
    print(eggs) #prints spam local

def bacon():
    eggs = 'bacon local' 
    print(eggs) #prints bacon local
    spam() #prints spam local
    print(eggs) #prints bacon local

eggs = 'global'
bacon() #prints bacon local\n spam local\n bacon local\n
print(eggs) #prints global

print()

def spam2():
    global eggs2
    eggs2 = 'spam' #this is global

def bacon2():
    eggs2 = 'bacon' #this is local

def ham2():
    print(eggs2) #prints the global

eggs2 = 42 #this is global
spam2()
print(eggs2) #prints spam. we set and then immediately overwrote global eggs2

print()

#try-catch

def trycatch(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error, invalid argument. Divide by zero not allowed.')

print(trycatch(2))
print(trycatch(12))
print(trycatch(0))
print(trycatch(1))

print()

def trycatch2(divideBy2):
    return 42 / divideBy2

try:
    print(trycatch(2))
    print(trycatch(12))
    print(trycatch(0))
    print(trycatch(1))
except ZeroDivisionError:
    print('Error, invalid argument. Divide by zero not allowed.')

print()

print('::::::::::::zig-zag::::::::::::')

import time, sys
indent = 0 #how many spaces to indent
indentIncreasing = True #whether the indent is increasing or not

try:
    while True: #main loop, run until user interrupt
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) #pause for 1/10th of a second

        if indentIncreasing:
            #increase the number of spaces
            indent = indent + 1
            if indent == 20:
                #change direction
                indentIncreasing = False
        else:
            #decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                #change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()

#practice questions

#1. 
#compartmentalization, organization, and deduplication of tasks, easier debugging. cleaner, faster code. 

#2.
#when the function is called
    
#3.
#def
    
#4.
#when a function is defined it is skipped, it only runs when called. a call is often just the name of the function followed by a () containing arguments (or not!)

#5.
#global scopes: 1
#local scopes: as many as there are functions

#6.
#they are destroyed

#7.
#the result of a function, usable in an expression or as an argument for another function

#8.
#None

#9.
#global eggs
 
#10.
#NoneType

#11.
#allows the current program to reference an external module called areallyourpetsnamederic
    
#12.
#spam.bacon()
    
#13.
#try and except error handling
    
#14.
#code to attempt goes in the try clause, code to run upon encountering an error goes in the except clause
    

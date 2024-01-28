print('Truth table: And Operator \n"True and True": ' + str(True and True) + '\n"True and False": ' + str(True and False) + '\n"False and True": ' + str(False and True) + '\n"False and False": ' + str(False and False))

print('\nTruth table: Or Operator \n"True or True": ' + str(True or True) + '\n"True or False": ' + str(True or False) + '\n"False or True": ' + str(False or True) + '\n"False or False": ' + str(False or False))

print('\nTruth table: Not Operator \n"not True": ' + str(not True) + '\n"not False": ' + str(not False))

print('\nBonus Round! Double Negatives: \n"not not True": ' + str(not not True) + '\n"not not False": ' + str(not not False))

print('\nLet\'s Mix Booleans and Comparison Operators: \n"(4 < 5) and (6 > 3)": ' + str((4 < 5 ) and (6 > 3)) + '\n"(4 < 5) and (9 < 6)": ' + str((4 < 5) and (9 < 6)) + '\n"(1 == 2) or (2 == 2)": ' + str((1 == 2) or (2 == 2)))

print('\nOne more time: \n"2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2": ' + str(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2))

print('\nOrder of operations matters here too! Not is evaluated first, And is evaluated next, and Or is evaluated last!')

validUsername = 'Mary'
correctPassword = 'swordfish'
age = 18
print('\nEnter your username:')
username = input()
if username == validUsername:
    print('Hello, ' + username + '! Enter your password:')
    password = input()
else:
    print('Hello, stranger...')
if username == validUsername and password == correctPassword:
    print('And how old are you?')
    inputAge = input()
    if int(inputAge) == age:
        print('Hello, Mary! Access Granted!')
    elif int(inputAge) < age:
        print('You are not Mary, Kiddo.')
    elif int(inputAge) > age:
        print('You\'re not Mary! You\'re old!')
else:
    print('Invalid Username or Password!')

def vamPy():
    name = 'Carol'
    age = 30
    print('\nWhat\'s your name?')
    inputName = input()
    print('\nHow old are you?')
    inputAge = input()
    if inputName == 'Alice' and int(inputAge) == age:
        print('\nHi, Alice.')
    elif int(inputAge) < 12:
        print('\nYou are not Alice, kiddo.')
    elif int(inputAge) > 2000:
        print('\nUnlike you, Alice is not an undead, immortal vampyre.')
    elif int(inputAge) > 100:
        print('\nYou are not Alice, Granny.')
    elif inputName == name and int(inputAge) == age:
        print('Welcome, Carol!')
    else:
        print('Get out of here dawg.\n')

vamPy()


def whilePy():
    spam = 0
    while spam <= 99:
        print('spamcount: ' + str(spam))
        spam = spam + 1
        if spam - 1 >= 40:
            break
    print('Mmm, spam.\n')

whilePy()

def continueWhilePy():
    while True:
        print('Who are you?')
        name = input()
        if name != 'Joe':
            continue
        print('Hello, Joe. What is the password?')
        password = input()
        if password == 'swordfish':
            break
    print('Access Granted.\n')

continueWhilePy()

def cateringPy():
    name = ''
    while not name:
        print('Enter your name.')
        name = input()
    print('How many guests will you have?')
    numOfGuests = int(input())
    if numOfGuests:
        print('Be sure to have enough room for all of your guests.')
    print('Done.\n')

cateringPy()

def rangerPyFor():
    print('My name is ')
    for i in range(5):
        print('Jimmy 5 Times (' + str(i + 1) + ')')

rangerPyFor()

def rangerPyWhile():
    print('\nMy name is ')
    i = 0
    while i < 5:
        print('Jimmy 5 Times (' + str(i + 1) + ')')
        i = i + 1

rangerPyWhile()

def rangerPyStartStopStep():
    print('\nCount from 10 to 30 (inclusive) by 2:')
    for i in range(10, 32, 2):
        print(i)

rangerPyStartStopStep()

def rangerPyCountDown():
    print('\nCount down from 10 to 0:')
    for i in range(10, -1, -1):
        print(i)

rangerPyCountDown()

def gaussPyFor():
    print('\nCount all the numbers up to 101:')
    total = 0
    for num in range(101):
        total = total + num
    print(total)

gaussPyFor()

def randomRange():
    import random #or "from random import *"
    print('\nGenerate 5 random numbers between 1 and 10:')
    for i in range(5):
        print(random.randint(1, 10))

randomRange()

def guessANumber():
    import random
    correct = random.randint(1, 10)
    guess = 0
    while guess != correct:
        print('\nI am thinking of a number between 1 and 10. What\'s your guess?')
        guess = int(input())
        if guess > correct:
            print('Too high!')
        elif guess < correct:
            print('Too low!')
        elif guess == correct:
            break
        else:
            print('No... Dawg...')
    print('Correct! The answer was ' + str(correct) + '!')

guessANumber()
    
def sysExit():
    import sys
    while True:
        print('Enter "exit" to exit.')
        response = input()
        if response == 'exit':
            sys.exit()
        print('You typed ' + response + '.')

sysExit()

#Practice questions:

#1:
#True and False, always capitalized, even though they won't be returned that way...

#2:
#and, or, not

#3:
#I did this in above code!

#4:
#False
#False
#True
#False
#False
#True

#5:
#==
#!=
#>
#>=
#<
#<=

#6:
#"=" assigns a value, "==" compares two values

#7:
#A condition follows a flow control statement and is evaluated to true or false. use when allowing your program to make decisions based on values/inputs

#8: 
#I can't read the indentations because it's split across two pages, but we're evaluating whether 0 is 10 or greater than 5. it's not, so we're ending up just printing "spam"

#9:
#spam = int(input())
#if spam == 1:
#   print('Hello')
#elif spam == 2:
#   print('Howdy')
#else:
#   print('Greetings!')

#10:
#Ctrl + D or Ctrl + C, context/env dependant

#11:
#continue re-evaluates the loop condition, break exits the loop and moves past its code block

#12:
#range(10) counts from 0 to 10
#range(0, 10) does the same, you've defined the start and stop as 0 and 10
#range(0, 10, 1) also does this, you've defined the start as 0, the stop as 10, and the interval as 1.
#all three output the same result

#13:
#for i in range(10):
#   print(i + 1)

#i = 1
#while i < 11:
#   print(i)

#14:
#spam.bacon()



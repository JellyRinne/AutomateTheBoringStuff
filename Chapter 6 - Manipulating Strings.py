spam = "This is Alice's Cat" #no escape char needed for ' using "s
spam = 'Say hi to Bob\'s mother' #escape char needed

print("Hello there!\nHow are you?\nI\'m doing fine.")

print()

print(r'That is Carol\'s cat') #r = raw string, escape chars don't work or matter
print(r'C:\Users\Jelatine\Downloads\carolcat.jpeg2000')

print()

print('''Dear Alice, 
      
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
      
Sincerely,
Bob''') #triple quotes allow for multiline strings, treated the same as raw strings 

print()

"""triple double quotes allow

for multi-line

comments"""

spam = 'Hello, world!'
print(spam[0])
print(spam[1])
print(spam[1])
print(spam[6])
print(spam[0])
print(spam[4])
print(spam[-1])

print()

fizz = spam[:5]
buzz = spam[7:]

if 'Hello' in spam:
    print(fizz)
    if 'world!' in spam:
        print(buzz)
else:
    print('wtf?')

print()

def stringspam():
    name = 'Al'
    age = '4000'
    print('Hello, my name is %s. I am %s years old' % (name, age))

stringspam()

print()

def stringspam2():
    name = 'Mike'
    age = '30'
    print(f'My name is {name}. I am {age} years old.')

stringspam2()

print()

def stringspam3():
    spam = "hello, world!"
    print(spam.upper())
    print(spam.lower())

stringspam3()

print()

def stringspam4():
    print('How are you?')
    feeling = input()
    if feeling.lower().upper().lower() == 'great':
        print('I feel great too')
    else:
        print('I hope the rest of your day is good')

stringspam4()

print()

def stringspam5():
    print('How are you?')
    feeling = input()
    if feeling.isupper() == True:
        print('Calm down, jackass.')
    else:
        print('kay thanks')

stringspam5()

print()

def stringspam6():
    print('enter some text')
    text = input()
    if text.isalpha():
        print('isAlpha')
    elif text.isalnum():
        print('isAlNum')
    elif text.isdecimal():
        print('isDecimal')
    elif text.isspace():
        print('isSpace')
    elif text.istitle():
        print('isTitle')
    else:
        print('wtf?')

stringspam6()

print()

def stringspam7():
    while True:
        print('Enter your age:')
        age = input()
        if age.isdecimal():
            break
        print('Please enter a number for your age.')

    while True:
        print('Select a new password (letters and numbers only):')
        password = input()
        if password.isalnum():
            break
        print('Passwords can only have letters and numbers.')

stringspam7()

print()


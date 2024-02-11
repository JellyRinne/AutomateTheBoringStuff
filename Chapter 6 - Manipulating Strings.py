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
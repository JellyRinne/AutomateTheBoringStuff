def listspam():
    spam = ['cat', 'bat', 'rat', 'elephant']
    i = 0
    while i < len(spam):
        print(spam[i])
        i = i + 1

listspam()

print()

def listspam2():
    import random
    spam = ['cat', 'bat', 'rat', 'elephant']
    i = 0
    while i < len(spam):
        print('The ' + spam[random.randint(0, len(spam) - 1)] + ' ate the ' + spam[random.randint(0, len(spam) - 1)] + '.')
        i = i + 1

listspam2()

print()
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

def listspam3():
    spam = [['cat', 'bat', 'rat'], [10, 20, 30, 40, 50]]
    print(spam[0])
    print(spam[0][1])
    print(spam[1][4])
    print(spam[-1][-2]) #negative ints are valid indexes too!
    print(spam[0][0:2]) #slice!
    print(spam[0][:2]) #slice, but more efficient
    print(spam[1][:]) #slice from beginning to end of the second list
    print(spam[0][1:])
    print(len(spam)) #how many values in spam?
    print(len(spam[0])) #how many values in the first list in spam?
    print(len(spam[1])) #how many values in the second?
    spam[0][1] = 'aardvark' #reassign a value
    print(spam)
    spam[0:1] = 'aardvark' #holy shit?? define the full range of a list as a string, and each index becomes a character in the string
    print(spam)

listspam3()

print()

def listspam4():
    spam = [1, 2, 3]
    spam2 = [4, 5, 6]
    print(spam + spam2)
    print(spam * 3)
    print((spam + spam2) * 3)
    spam = spam + [4, 5, 6]
    print(spam)

listspam4()

print()

def listspam5():
    spam = [1, 2, 3, 4, 5, 6]
    print(spam)
    del spam[4]
    print(spam)

listspam5()

print()

def listspam6():
    catNames = []
    while True:
        print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
        name = input()
        if name == '':
            break
        catNames = catNames + [name] #add the cat to the list
    print('The cat names are:')
    for name in catNames:
        print('-' + name)

listspam6()

print()

def listspam7():
    for i in range(4):
        print(i)
    for i in [0, 1, 2, 3]:
        print(i)

listspam7()

print()

def listspam9():
    supplies = ['paper', 'staples', 'paperclips', 'post-its']
    for i in range(len(supplies)):
        print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

listspam9()
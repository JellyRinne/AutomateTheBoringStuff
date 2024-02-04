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

print()

def listspam10():
    spam = []
    while True:
        print('Enter the species of animal ' + str(len(spam) + 1) + ' (Or enter nothing to stop.):')
        name = input()
        if name == '':
            break
        spam = spam + [name] #add the cat to the list
    print('Is there a cat?')
    if 'cat' in spam:
        print('Yes')
    elif 'cat' not in spam:
        print('No')
    else:
        print('I can\'t tell???')

listspam10()

print()

def listspam11():
    cat = ['fat', 'gray', 'loud']
    size, color, disposition = cat
    print('The cat\'s size is: ' + size)
    print('The cat\'s color is: ' + color)
    print('The cat\'s disposition is: ' + disposition)

listspam11()

print()

def listspam12():
    supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
    for index, item in enumerate(supplies):
        print('Index ' + str(index) + ' in supplies is: ' + item)

listspam12()

print()

def listspam13():
    import random
    pets = ['cats', 'dogs', 'rats']
    print('The best pets are ' + random.choice(pets))
    random.shuffle(pets)
    print('But my favorite pets are: ' + str(pets))

listspam13()

print()

def listspam14():
    print('"spam += 1" is the same as "spam = spam + 1"')
    print('"spam -= 1" is the same as "spam = spam - 1"')
    print('"spam *= 1" is the same as "spam = spam * 1"')
    print('"spam /= 1" is the same as "spam = spam / 1"')
    print('"spam %= 1" is the same as "spam = spam % 1"')
    spam = 'Hello, '
    spam += 'World!'
    print(spam)
    bacon = ['ham']
    bacon *= 3
    print(bacon)

listspam14()

print()

def listspam15():
    spam = ['ham', 'bacon', 'eggs']
    extraProteins = ['sausage', 'steak', 'tofu']
    spam.insert(3, 'toast')
    i = 0
    for index, protein in enumerate(spam):
        print('The index of \'' + protein + '\' is: ' + str(spam.index(protein)))
        if i < len(extraProteins):
            spam.append(extraProteins[i])
            i += 1
            spam.remove(spam[0])        

listspam15()

print()

def listspam16():
    spam = [2, 5, 3.14,
                                     1, 
                -7]
    print(str(spam) + ' sorted is:')
    spam.sort()
    print(spam)
    print()
    spam2 = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
    print(str(spam2) + ' sorted backwards is:')
    spam2.sort(reverse=True) #ASCIIbetical sort
    print(spam2)
    print()
    print(str(spam) + ' sorted backwards is:')
    spam.reverse()
    print(spam)

listspam16()

print()

def listspam17():
    import random
    messages = ['It is certain',
                'Yes definitely',
                'Reply hazy, try again',
                'Ask again later',
                'Concentrate and ask again',
                'My reply is no',
                'Outlook not so good',
                'Very doubtful']
    print(messages[random.randint(0, len(messages) - 1)])

listspam17()

print()

def listspam18():
    name = 'Roger Persona'
    for i in name: #strings are lists!
        print('***' + i + '***')

listspam18()

print()

def listspam19():
    name = 'John Persona'
    newName = name[0:4] + ' the ' + name[5:12]
    print(newName)

listspam19()

print()

def listspam20(): #tuple, actually
    eggs = ('hello', 42, 0.5) #immutable values in an immutable list, faster than lists too
    spam = ('spam',) #comma denotes tuple with single value
    bacon = 'ham'
    print(bacon)
    print(tuple(bacon))
    print(list(bacon))

listspam20()

print()

def listspam21(): #lists aren't quite like other data types...
    spam = 42
    cheese = spam
    spam = 100
    print(cheese)
    #vs
    bacon = [0, 1, 2, 3, 4, 5]
    eggs = bacon
    bacon[1] = 24
    print(eggs)

listspam21()

print()

def listspam22():
    print(id('howdy!'))

listspam22()

print()

def listspam23(someParameter):
    someParameter.append('Hello!')

spam = [1, 2, 3]
listspam23(spam)
print(spam)

print()

def listspam24():
    import copy
    bacon = [1, 2, 3, 4]
    print(str(bacon) + ' ID:')
    print(id(bacon))
    eggs = bacon
    print('eggs is a reference to bacon: ' + str(eggs) + ' and its ID is:')
    print(id(eggs))
    spam = ['A', 'B', 'C', 'D',]
    print(str(spam) + ' ID:')
    print(id(spam))
    cheese = copy.copy(spam) #copy.deepcopy() is necessary for lists that contains lists
    print('cheese is a copy of spam: ' + str(cheese) + ' and its ID is:')
    print(id(cheese))

listspam24()

#Practice Questions:

#1.
#An empty list

#2. 
#spam[2] = 'hello'

#3.
#'d'

#4.
#'d'

#5.
#'a', 'b'

#6.
#1

#7.
#[3.14, 'cat', 11, 'cat, True, 99]

#8.
#[3.14, 11, 'cat', True]

#9.
#+, *

#10.
#append adds a value to the end of a list, insert takes an integer for the index of where to insert the chosen value

#11.
# del * .remove()

#12.
#a string is a list of characters and a list is a string of values

#13.
#lists are mutable, tuples are not

#14.
#spam = (42,)

#15.
#tuple(listName)
#list(tupleName)

#16.
#references to the list

#17.
#copy will not copy the values of lists within lists, deepcopy will
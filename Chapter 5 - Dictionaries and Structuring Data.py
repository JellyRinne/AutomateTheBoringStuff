def dictspam():
    myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
    print ('My ' + myCat['color'] + ' cat is ' + myCat['size'] + ' and ' + myCat['disposition'])

dictspam()

print()

def dictspam2():
    eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
    ham = {'age': 8, 'name': 'Zophie', 'species': 'cat'}

    print(eggs)
    print(ham)
    if eggs == ham:
        print('These are the same!')

dictspam2()

print()

def dictspam3():
    birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

    while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break

        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('BirthDB updated.')

dictspam3()

print()

def dictspam4():
    spam = {'color': 'red', 'age': 42}
    for k in spam.keys():
            print(k)
    for v in spam.values():
            print(v)
    for i in spam.items():
            print(i)
    for k, v in spam.items():
         print('Key: ' + k + ', Value: ' + str(v))

dictspam4()

print()

def dictspam5():
     picnicItems = {'apples': 5, 'cups': 2}
     print('I am bringing ' + str(picnicItems.get('apples', 0)) + ' apples') 
     print('and ' + str(picnicItems.get('cups', 0)) + ' cups.')
     print('I might bring ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
     picnicItems.setdefault('eggs', 42)
     print('On the other hand, I might bring ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

dictspam5()

print()

def dictspam6():
    import pprint
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}
    for character in message:
         count.setdefault(character, 0)
         count[character] += 1

    pprint.pprint(count)
    print(pprint.pformat(count))

dictspam6()

print()

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])

def turn():
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    printBoard(theBoard)

turn()

print()
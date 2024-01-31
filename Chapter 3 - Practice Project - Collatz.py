def collatz(number):
    if number % 2 == 0:
        print(str(number // 2))
        return number // 2
    else:
        print(3 * number +1)
        return 3 * number + 1

def collatzer():
    print('\nEnter a number:')
    try:
        testNumber = int(input())
        while True:
            testNumber = collatz(testNumber)
            if testNumber == 1:
                break
            else:
                continue
    except ValueError:
        print('Invalid input, please enter an integer.')
        collatzer()
    
collatzer()
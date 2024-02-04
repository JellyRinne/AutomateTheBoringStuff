def listspam(listName):
    outStr = ''
    for i, value in enumerate(listName):
        if i == len(listName) - 1:
            outStr = outStr + value
        else: 
            outStr = outStr + value + ' and '
    print(outStr)

spam = ['apples', 'bananas', 'tofu', 'cats']
listspam(spam)

import pprint

myInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        string = str(v) + ' ' + str(k)
        print(string)
        item_total = item_total + int(v)
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addeditems):
    newInventory = {}
    for k, v in inventory.items():
        newInventory.setdefault(k, v)
    for i in range(len(addeditems)):
        if addeditems[i] not in newInventory:
            newInventory.setdefault(addeditems[i], 1)
        else:
            newInventory[addeditems[i]] += 1
    return newInventory

displayInventory(myInventory)        

print()

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)


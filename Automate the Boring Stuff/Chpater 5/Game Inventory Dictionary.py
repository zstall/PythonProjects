'''
Inventory Dictionary

Chapter 5 Pg. 120

Practice printing all the key and values of a dictionary:
This is a 'video game' inventory, and there is a method that
will print out all keys and values.
'''

import pprint

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    print('********************************************')
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += 1
    print('Total Inventory: ' + str(item_total))
    print('********************************************')
    print()
    
def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1
        
displayInventory(stuff)
addToInventory(stuff, dragonLoot)
displayInventory(stuff)

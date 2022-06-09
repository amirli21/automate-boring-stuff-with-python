# Write your code here :-)
def displayInventory(inventory):
    total_items = sum(inventory.values())
    for item in inventory:
        print(inventory[item], item, sep=' ')
    print('Total number of items '+str(total_items))



def addToInventory(inventory, addedItems):
    total_added_items = len(addedItems)
    total_items = sum(inventory.values()) + total_added_items
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


inventory = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)

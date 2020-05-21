#Write a function named display_inventory() that would take any possible 'inventory' and display it as following : ATBS page 127

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print(f'Total number of items: {item_total}')

#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#display_inventory(stuff)

#Write a fucntion named add_to_inventory(inventory, added_items), where the dictionary representing the players inventory is updated to contain the new loot
def add_items_to_inventory(inventory, loot):
    #lets add the loot to our inventory and add 1 to the value
    for item in loot:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory



inv = {'gold coin': 42, 'rope':1}
# dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = add_items_to_inventory(inv, dragon_loot)
# display_inventory(inv)
slime_loot = ['rusty coin']
inv = add_items_to_inventory(inv, slime_loot)
display_inventory(inv)


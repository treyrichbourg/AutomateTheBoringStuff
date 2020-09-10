all_guests = {'Alice': {'apples': 5, 'pretzels': 12}, 'Bob': {'ham sandwiches': 3, 'apples': 2}, 'Carol': {'cups': 3, 'apple pies': 1}}
#loops through the dictionary, _ is assigned to the name of the guests while v is assigned to the nested dictionaries or key/value pairs
def total_brought(guests, item):
    num_brought = 0 #counter
    for _, v in guests.items():  
        num_brought += v.get(item,0) #looks for the value of the item and adds it to num_brought
    return num_brought

print('Number of things being brought:')
print(f" - Apples            {total_brought(all_guests, 'apples')}")
print(f" - Pretzels          {total_brought(all_guests, 'pretzels')}")
print(f" - Cups              {total_brought(all_guests, 'cups')}")
print(f" - Cakes             {total_brought(all_guests, 'cakes')}")
print(f" - Ham Sandwiches    {total_brought(all_guests, 'ham sandwiches')}")
print(f" - Apple Pies        {total_brought(all_guests, 'apple pies')}")

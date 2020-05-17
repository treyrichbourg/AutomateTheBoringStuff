#original grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#Want to print this using values from the list above
# ..00.00..
# .0000000.
# .0000000.
# ..00000..
# ...000...
# ....0....


for x in range(len(grid[0])): #loop through the current x values, will become our 'y' 
    for y in range(0, len(grid)): #loop and grab values for what will become our 'x' 
        if y < 8: #loops and grabs values 0 - 7 and prints in single line
            print(grid[y][x], end = '')
        else: #this will grab the item in value 8, return a line break, then go back to the original loop so we can get a new line
            print(grid[y][x])

# def heart():
#     for x in range(len(grid[0])):
#         for y in range(0, len(grid)):
#             if y < 8:
#                 print(grid[y][x], end = '')
#             else:
#                 print(grid[y][x])

# print(heart())
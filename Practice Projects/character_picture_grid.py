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

for x in range(len(grid[0])):
    for y in range(0, len(grid)):
        if y < 8:
            print(grid[y][x], end = '')
        else:
            print(grid[y][x])

def heart():
    for x in range(len(grid[0])):
        for y in range(0, len(grid)):
            if y < 8:
                print(grid[y][x], end = '')
            else:
                print(grid[y][x])

print(heart())
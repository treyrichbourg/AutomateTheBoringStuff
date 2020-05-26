#! python3
#Write a function that takes a list of lists of strings and displays it in a well-organized table with each column right-justified.

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def print_table(data):
    #create a list containing the same number of 0 values as the number of inner lists in table_data.  
    #This list can store the width of the longest string in each list from table_data.
    column_widths = [0] * len(table_data)
    #Find the length of the longest string in each list in table_data
    for value_set in range(len(data)):
        for string in range(len(data[value_set])):
            if len(data[value_set][string]) > column_widths[value_set]:
                column_widths[value_set] = len(data[value_set][string])
    print(column_widths)
    #return each list inside the data in a 'table' using .rjust(column_width) for each appropriate iteration
    #make a variable to store the index of each list inside the data
    data_index = [i for i in range(len(table_data))]




print(print_table(table_data))





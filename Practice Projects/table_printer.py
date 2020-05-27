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
    #print(column_widths)
    #return each list inside the data in a table using .rjust(column_width) for each appropriate iteration
    #make a variable to tell the loop when to line break
    number_of_columns = len(data) - 1
    #loop through the length of the first index in data
    for word in range(len(data[0])):    
        for column in range(len(data)):
            if column < number_of_columns:
                print(data[column][word].rjust(column_widths[column]), end = ' ')
            else:
                print(data[column][word].rjust(column_widths[column]))

print_table(table_data)




